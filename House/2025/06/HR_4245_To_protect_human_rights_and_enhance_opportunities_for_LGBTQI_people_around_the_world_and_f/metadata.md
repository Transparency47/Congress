# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4245?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4245
- Title: GLOBE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4245
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-01-10T06:41:05Z
- Update date including text: 2026-01-10T06:41:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4245",
    "number": "4245",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "GLOBE Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-10T06:41:05Z",
    "updateDateIncludingText": "2026-01-10T06:41:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-27T13:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "DC"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "GA"
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
      "sponsorshipDate": "2025-06-27",
      "state": "GA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "VT"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "MA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "VA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "WI"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "PA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "WA"
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
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MN"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NJ"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "IL"
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
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "KS"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
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
      "sponsorshipDate": "2025-06-27",
      "state": "MA"
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
      "sponsorshipDate": "2025-06-27",
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
      "sponsorshipDate": "2025-06-27",
      "state": "WA"
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
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CT"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "RI"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "IL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "DE"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NV"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4245ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4245\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Ms. Titus (for herself, Mr. McGovern , Mr. Pocan , Mrs. Ramirez , Mr. Huffman , Ms. Norton , Mr. Garcia of California , Ms. Crockett , Ms. Tlaib , Ms. Simon , Ms. Williams of Georgia , Mr. Johnson of Georgia , Ms. Balint , Mr. Costa , Mr. Mullin , Mr. Keating , Mr. Khanna , Ms. Chu , Ms. McClellan , Ms. Moore of Wisconsin , Mr. Cohen , Mr. Casten , Ms. Dean of Pennsylvania , Ms. Strickland , Mr. Schneider , Ms. Jacobs , Ms. Omar , Mr. Moulton , Mr. Gottheimer , Mr. Krishnamoorthi , Mr. Peters , Ms. Davids of Kansas , Ms. Brownley , Mr. Castro of Texas , Mr. Lieu , Mr. Kennedy of New York , Mr. Lynch , Mr. Goldman of New York , Ms. Jayapal , Mrs. Torres of California , Ms. Barrag\u00e1n , Mrs. Hayes , and Mr. Nadler ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo protect human rights and enhance opportunities for LGBTQI people around the world, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Greater Leadership Overseas for the Benefit of Equality Act of 2025 or the GLOBE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States has been and must always be the global leader in protecting human rights, including the rights of lesbian, gay, bisexual, transgender, queer, and intersex (LGBTQI) peoples around the world.\n**(2)**\nThe norms of good governance, human rights protections, and the rule of law have been violated unconscionably with respect to LGBTQI peoples in an overwhelming majority of countries around the world, where LGBTQI people face violence, hatred, bigotry, and discrimination because of who they are and whom they love.\n**(3)**\nIn at least 62 countries, or roughly 32 percent of the world, same-sex relations and relationships are criminalized. Many countries also criminalize or otherwise prohibit cross-dressing and gender-affirming treatments for transgender individuals.\n**(4)**\nThe World Bank has begun to measure the macro-economic costs of criminal laws targeting LGBTQI individuals through lost productivity, detrimental health outcomes and violence, as a step toward mitigating those costs.\n**(5)**\nViolence and discrimination based on sexual orientation and gender identity are documented in the Department of State\u2019s annual Country Human Rights Reports to Congress. These reports continue to show a clear pattern of human rights violations, including murder, rape, torture, death threats, extortion, and imprisonment, in every region of the world based on sexual orientation and gender identity. In many instances police, prison, military, and civilian government authorities have been directly complicit in abuses aimed at LGBTQI citizens.\n**(6)**\nAs documented by the State Department, LGBTQI individuals are subjected in many countries to capricious imprisonment, loss of employment, housing, access to health care, societal stigma, and discrimination. LGBTQI-specific restrictions on basic freedoms of assembly, press, and speech exist in every region of the world.\n**(7)**\nTargeted sanctions are an important tool to push for accountability for violations of the human rights of LGBTQI people.\n**(8)**\nAnti-LGBTQI laws and discrimination pose significant risks for LGBTQI youth who come out to their family or community and often face rejection, homelessness, and limited educational and economic opportunities. These factors contribute to increased risks of substance abuse, suicide, and HIV infection among LGBTQI youth.\n**(9)**\nAnti-LGBTQI laws also increase global health risks. Studies have shown that when LGBTQI people, especially LGBTQI youth, face discrimination, they are less likely to seek HIV testing, prevention, and treatment services.\n**(10)**\nLGBTQI populations are disproportionately impacted by the Mexico City Policy, also widely referred to as the global gag rule . LGBTQI people often receive much of their health care through reproductive health clinics, and organizations that cannot comply with the policy are forced to discontinue work on United States-supported global health projects that are frequently used by LGBTQI populations, including HIV prevention and treatment, stigma reduction, and research.\n**(11)**\nAt the beginning of his second term, President Donald Trump reinstated the global gag rule before abruptly terminating nearly all foreign aid contracts.\n**(12)**\nBecause they face tremendous discrimination in the formal labor sector, many sex workers are also LGBTQI individuals, and many sex-worker-led programs and clinics serve the LGBTQI community with safe, non-stigmatizing, medical and social care. USAID has also referred to sex workers as a most-at-risk population . The anti-prostitution loyalty oath that health care providers receiving United States assistance must take isolates sex-worker-led and serving groups from programs and reinforces stigma, undermining both the global AIDS response and human rights. The Supreme Court found this requirement unconstitutional as it applies to United States nongovernmental organizations and their foreign affiliates in 2013.\n**(13)**\nAccording to the Trans Murder Monitoring Project, which monitors homicides of transgender individuals, there were at least 350 cases of reported killings of trans and gender-diverse people between October 1, 2023, and September 30, 2024.\n**(14)**\nIn many countries, intersex individuals experience prejudice and discrimination because their bodies do not conform to general expectations about sex and gender. Because of these expectations, medically unnecessary interventions are often performed in infancy without the consent or approval of intersex individuals, in violation of international human rights standards, and are then often denied official identification papers, blocking them from accessing basic services and legal protections.\n**(15)**\nAsylum and refugee protection are critical last-resort protections for LGBTQI individuals, but those who seek such protections face ostracization and abuse in refugee camps and detention facilities. They are frequently targeted for violence, including sexual assault, in refugee camps and in immigration detention. LGBTQI individuals may be segregated against their will for long periods in solitary confinement, in an effort to protect them from such violence, but prolonged solitary confinement itself represents an additional form of abuse that is profoundly damaging to the social and psychological well-being of any individual.\n**(16)**\nThe global COVID\u201319 pandemic exacerbated inequalities that LGBTQI individuals face, including access to health care, stigma, and discrimination, undermining LGBTQI rights around the world.\n**(17)**\nIn December 2011, President Barack Obama directed all Federal foreign affairs agencies to ensure that their diplomatic, humanitarian, health and foreign assistance programs take into account the needs of marginalized LGBTQI communities and persons.\n**(18)**\nIn 2015, the Department of State established the position of Special Envoy for the Human Rights of LGBTQI Persons.\n**(19)**\nIn 2021, President Joseph Biden issued the Memorandum on Advancing the Human Rights of Lesbian, Gay, Bisexual, Transgender, Queer, and Intersex Persons Around the World, which stated that it is the policy of the United States to pursue an end to violence and discrimination on the basis of sexual orientation, gender identity or expression, or sex characteristics and called for United States global leadership on LGBTQI rights.\n**(20)**\nIn Bostock v. Clayton County, the Supreme Court held that title VII of the Civil Rights Act of 1964 prohibits discrimination on the basis of gender identity and sexual orientation. On January 20, 2021, President Biden issued Executive Order 13988 to enforce Bostock, which orders all agency heads to determine the additional steps they should take to ensure that administration policies are fully implemented consistent with Bostock, including the Secretary of State and the Administrator of USAID.\n**(21)**\nThe use of United States diplomatic tools, including the Department of State\u2019s exchange and speaker programs, to address the human rights needs of marginalized communities has helped inform public debates in many countries regarding the protective responsibilities of any democratic government.\n**(22)**\nInclusion of human rights protections for LGBTQI individuals in United States trade agreements, as in the United States-Mexico-Canada Agreement, and trade preference programs is intended both to ensure a level playing field for United States business and to provide greater workplace protections overseas, compatible with those of the United States.\n**(23)**\nEngaging multilateral fora and international institutions is critical to impacting global norms and to broadening global commitments to fairer standards for the treatment of all people, including LGBTQI people. The United States must remain a leader in the United Nations system and has a vested interest in the success of that multilateral engagement.\n**(24)**\nUnited States participation in the Equal Rights Coalition, which is a new intergovernmental coalition of more than 40 governments and leading civil society organizations that work together to protect the human rights of LGBTQI people around the world, is vital to international efforts to respond to violence and impunity.\n**(25)**\nThose who represent the United States abroad, including our diplomats, development specialists and military, should reflect the diversity of our country and honor the United States call to equality, including through proud and open service abroad by LGBTQI United States citizens and those living with HIV.\n#### 3. Documenting and responding to bias-motivated violence against lgbtqi people abroad\n##### (a) Information required To be included in annual country reports on human rights practices\n**(1) Section 116**\nSection 116(d) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151n(d) ) is amended\u2014\n**(A)**\nin paragraph (11)(C), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (12)(C)(ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(13) wherever applicable, the nature and extent of criminalization, discrimination, and violence by state and non-state actors based on sexual orientation or gender identity, as those terms are defined in section 12 of GLOBE Act of 2025 , or sex characteristics, including an identification of those countries that have adopted laws or constitutional provisions that criminalize or discriminate based on sexual orientation, gender identity, or sex characteristics, including descriptions of such laws and provisions. .\n**(2) Section 502b**\nSection 502B of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2304 ) is amended\u2014\n**(A)**\nby redesignating the second subsection (i) (relating to child marriage status) as subsection (j); and\n**(B)**\nby adding at the end the following new subsection:\n(k) Sexual orientation, gender identity, and sex characteristics The report required under subsection (b) shall include, wherever applicable, the nature and extent of criminalization, discrimination, and violence by state and non-state actors based on sexual orientation or gender identity, as those terms are defined in section 12 of the GLOBE Act of 2025 , or sex characteristics, including an identification of those countries that have adopted laws or constitutional provisions that criminalize or discriminate based on sexual orientation, gender identity, or sex characteristics, including descriptions of such laws and provisions. .\n##### (b) Review at diplomatic and consular posts\n**(1) In general**\nIn preparing the annual country reports on human rights practices required by section 116 or 502B of the Foreign Assistance Act of 1961, as amended by subsection (a), the Secretary of State shall obtain information from each diplomatic and consular post with respect to the following:\n**(A)**\nIncidents of violence against LGBTQI people in the country in which such post is located.\n**(B)**\nAn analysis of the factors enabling or aggravating such incidents, such as government policy, societal pressure, or external actors.\n**(C)**\nThe response, whether public or private, of the personnel of such post with respect to such incidents.\n**(2) Addressing bias-motivated violence**\nThe Secretary shall include in the annual strategic plans of the regional bureaus concrete diplomatic strategies, programs, and policies to address bias-motivated violence using information obtained pursuant to paragraph (1), such as programs to build capacity among civil society or governmental entities to document, investigate, and prosecute instances of such violence and provide support to victims of such violence.\n##### (c) Interagency group\n**(1) Establishment**\nThere is established an interagency group on responses to urgent threats to LGBTQI people in foreign countries (in this subsection referred to as the interagency group ), that shall be chaired by the Secretary of State and include the Secretary of Defense, the Secretary of the Treasury, the Administrator of the United States Agency for International Development, the Attorney General, and the head of each other Federal department or agency the President determines is relevant to the duties of the interagency group.\n**(2) Duties**\nThe duties of the interagency group shall be to\u2014\n**(A)**\ncoordinate the responses of each participating agency with respect to threats directed towards LGBTQI populations in other countries;\n**(B)**\ndevelop longer-term approaches to policy developments and incidents negatively impacting the LGBTQI populations in specific countries;\n**(C)**\nadvise the President on the designation of foreign persons for sanctions pursuant to section 4;\n**(D)**\nidentify United States laws and policies, at the Federal, State, and local levels, that affirm the equality of LGBTQI persons; and\n**(E)**\nuse such identified laws and policies to develop diplomatic strategies to share the expertise obtained from the implementation of such laws and policies with appropriate officials of countries where LGBTQI persons do not enjoy equal protection under the law.\n##### (d) Special envoy for the human rights of LGBTQI peoples\n**(1) Establishment**\nThe Secretary of State shall establish in the Bureau of Democracy, Human Rights, and Labor of the Department of State a permanent Special Envoy for the Human Rights of LGBTQI Peoples (in this section referred to as the Special Envoy ), who\u2014\n**(A)**\nshall be appointed by the President; and\n**(B)**\nshall report directly to the Assistant Secretary for Democracy, Human Rights, and Lab.\n**(2) Rank**\nThe President may appoint the Special Envoy at the rank of Ambassador, by and with the advice and consent of the Senate.\n**(3) Purpose**\nThe Special Envoy shall direct efforts of the United States Government relating to United States foreign policy, as directed by the Secretary, regarding human rights abuses against LGBTQI people and communities internationally and the advancement of human rights for LGBTQI people, and shall represent the United States internationally in bilateral and multilateral engagement on such matters.\n**(3) Duties**\nThe Special Envoy shall\u2014\n**(A)**\nserve as the principal advisor to the Secretary of State regarding human rights for LGBTQI people internationally;\n**(B)**\nnotwithstanding any other provision of law, direct activities, policies, programs, and funding relating to the human rights of LGBTQI people and the advancement of LGBTQI equality initiatives internationally, for all bureaus and offices of the Department of State and shall lead the coordination of relevant international programs for all other Federal agencies relating to such matters;\n**(C)**\nrepresent the United States in diplomatic matters relevant to the human rights of LGBTQI people, including criminalization, discrimination, and violence against LGBTQI people internationally;\n**(D)**\ndirect, as appropriate, United States Government resources to respond to needs for protection, integration, resettlement, and empowerment of LGBTQI people in United States Government policies and international programs, including to prevent and respond to criminalization, discrimination, and violence against LGBTQI people internationally;\n**(E)**\ndesign, support, and implement activities regarding support, education, resettlement, and empowerment of LGBTQI people internationally, including for the prevention and response to criminalization, discrimination, and violence against LGBTQI people internationally;\n**(F)**\nlead interagency coordination between the foreign policy priorities related to the human rights of LGBTQI people and the development assistance priorities of the LGBTQI Coordinator of the United States Agency for International Development;\n**(G)**\nconduct regular consultation with nongovernmental organizations working to prevent and respond to criminalization, discrimination, and violence against LGBTQI people internationally; and\n**(H)**\nrepresent the United States in bilateral and multilateral fora on matters relevant to the human rights of LGBTQI people internationally, including criminalization, discrimination, and violence against LGBTQI people internationally.\n##### (e) Training at international law enforcement academies\nThe President shall ensure that any international law enforcement academy supported by United States assistance shall provide training with respect to the rights of LGBTQI people, including through specialized courses highlighting best practices in the documentation, investigation, and prosecution of bias-motivated hate crimes targeting persons based on actual or perceived sexual orientation, gender identity, or sex characteristics.\n##### (f) Senior LGBTQI coordinator\nThe Administrator of the United States Agency for International Development shall establish a permanent Senior LGBTQI Coordinator who shall be appointed by the Administrator and will coordinate across the agency with respect to LGBTQI inclusive development programming.\n#### 4. Sanctions on individuals responsible for violations of human rights against lgbtqi people\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act and biannually thereafter, the President shall transmit to the appropriate congressional committees a list of each foreign person the President determines, based on credible information, including information obtained by other countries or by nongovernmental organizations that monitor violations of human rights\u2014\n**(1)**\nis responsible for or complicit in, with respect to persons based on actual or perceived sexual orientation, gender identity, or sex characteristics\u2014\n**(A)**\ntorture or cruel, inhuman, or degrading treatment or punishment;\n**(B)**\nprolonged detention without charges and trial;\n**(C)**\ncausing the disappearance of such persons by the abduction and clandestine detention of such persons; or\n**(D)**\nother flagrant denial of the right to life, liberty, or the security of such persons; or\n**(2)**\nacted as an agent of or on behalf of a foreign person in a matter relating to an activity described in paragraph (1).\n##### (b) Form; updates; removal\n**(1) Form**\nThe list required by subsection (a) shall be transmitted in unclassified form and published in the Federal Register without regard to the requirements of section 222(f) of the Immigration and Nationality Act ( 8 U.S.C. 1202(f) ) with respect to confidentiality of records pertaining to the issuance or refusal of visas or permits to enter the United States, except that the President may include a foreign person in a classified, unpublished annex to such list if the President\u2014\n**(A)**\ndetermines that\u2014\n**(i)**\nit is vital for the national security interests of the United States to do so; and\n**(ii)**\nthe use of such annex, and the inclusion of such person in such annex, would not undermine the overall purpose of this section to publicly identify foreign persons engaging in the conduct described in subsection (a) in order to increase accountability for such conduct; and\n**(B)**\nnot later than 15 days before including such person in a classified annex, provides to the appropriate congressional committees notice of, and a justification for, including or continuing to include each foreign person in such annex despite the existence of any publicly available credible information indicating that each such foreign person engaged in an activity described in subsection (a).\n**(2) Updates**\nThe President shall transmit to the appropriate congressional committees an update of the list required by subsection (a) as new information becomes available.\n**(3) Removal**\nA foreign person may be removed from the list required by subsection (a) if the President determines and reports to the appropriate congressional committees not later than 15 days before the removal of such person from such list that\u2014\n**(A)**\ncredible information exists that such person did not engage in the activity for which the person was included in such list;\n**(B)**\nsuch person has been prosecuted appropriately for the activity in which such person engaged;\n**(C)**\nsuch person has credibly demonstrated a significant change in behavior, has paid an appropriate consequence for the activities in which such person engaged, and has credibly committed to not engage in an activity described in subsection (a); or\n**(D)**\nremoval of such sanctions is in the vital national security interests of the United States.\n##### (c) Public submission of information\nThe President shall issue public guidance, including through United States diplomatic and consular posts, setting forth the manner by which the names of foreign persons that may meet the criteria to be included on the list required by subsection (a) may be submitted to the Department of State for evaluation.\n##### (d) Requests from chair and ranking member of appropriate congressional committees\n**(1) Consideration of information**\nIn addition to the guidance issued pursuant to subsection (c), the President shall also consider information provided by the Chair or Ranking Member of each of the appropriate congressional committees in determining whether to include a foreign person in the list required by subsection (a).\n**(2) Requests**\nNot later than 120 days after receiving a written request from the Chair or Ranking Member of 1 of the appropriate congressional committees with respect to whether a foreign person meets the criteria for being included in the list required by subsection (a), the President shall transmit a response to such Chair or Ranking Member, as the case may be, with respect to the President\u2019s determination relating to such foreign person.\n**(3) Removal**\nIf the President removes from the list required by subsection (a) a foreign person that had been included in such list pursuant to a request under paragraph (2), the President shall provide to the relevant Chair or Ranking Member of 1 of the appropriate congressional committees any information that contributed to such decision.\n**(4) Form**\nThe President may transmit a response required by paragraph (2) or paragraph (3) in classified form if the President determines that it is necessary for the national security interests of the United States to do so.\n##### (e) Inadmissibility of certain individuals\n**(1) Ineligibility for visas and admission to the united states**\nA foreign person on the list required by subsection (a), and each immediate family member of such person, is\u2014\n**(A)**\ninadmissible to the United States;\n**(B)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(C)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(2) Current visas revoked**\n**(A) In general**\nThe issuing consular officer or the Secretary of State (or a designee of the Secretary of State) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to a foreign person on the list required by subsection (a), and any visa or other entry documentation issued to any immediate family member of such person, regardless of when the visa or other entry documentation is issued.\n**(B) Effect of revocation**\nA revocation under subparagraph (A) shall\u2014\n**(i)**\ntake effect immediately; and\n**(ii)**\nautomatically cancel any other valid visa or entry documentation that is in the foreign person\u2019s possession.\n**(C) Regulations required**\nNot later than 180 days after the date of enactment of this Act, the Secretary of State shall prescribe such regulations as are necessary to carry out this subsection.\n**(3) Sense of congress with respect to additional sanctions**\nIt is the sense of Congress that the President should impose additional targeted sanctions with respect to foreign persons on the list required by subsection (a) to push for accountability for flagrant denials of the right to life, liberty, or the security of the person, through the use of designations and targeted sanctions provided for such conduct under other existing authorities.\n**(4) Exceptions**\n**(A) Exception with respect to national security**\nThis section shall not apply with respect to\u2014\n**(i)**\nactivities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(ii)**\nany authorized intelligence or law enforcement activities of the United States.\n**(B) Exception to comply with international obligations**\nSanctions under this subsection shall not apply with respect to a foreign person if admitting or paroling such person into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success, June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(C) Exception for certain immediate family members**\n**(i) In general**\nA covered individual shall not be subject to sanctions under this section if the President certifies to the appropriate congressional committees, in accordance with clause (ii), that such individual has a reasonable fear of persecution based on\u2014\n**(I)**\nactual or perceived sexual orientation, gender identity, or sex characteristics;\n**(II)**\nrace, religion, or nationality; or\n**(III)**\npolitical opinion or membership in a particular social group.\n**(ii) Determination and certification**\nA certification under clause (i) shall be made not later than 30 days after the date of the determination required by such clause. Any proceedings relating to such determination shall not be publicly available.\n**(iii) Covered individual**\nFor purposes of this subparagraph, the term covered individual means an individual who is an immediate family member of foreign person on the list required by subsection (a).\n**(4) Waivers in the interest of national security**\n**(A) In general**\nThe President may waive the application of paragraph (1) or (2) with respect to a foreign person included in the list required by subsection (a) if the President determines and transmits to the appropriate congressional committees notice and justification, that such a waiver\u2014\n**(i)**\nis necessary to permit the United States to comply with the Agreement between the United Nations and the United States regarding the Headquarters of the United Nations, signed June 26, 1947, and entered into force November 21, 1947, or other applicable international obligations of the United States; or\n**(ii)**\nis in the national security interests of the United States.\n**(B) Timing of certain waivers**\nA waiver pursuant to a determination under clause (ii) of subparagraph (A) shall be transmitted not later than 15 days before the granting of such waiver.\n##### (f) Report to congress\nNot later than 1 year after the date of enactment of this Act and annually thereafter, the President, acting through the Secretary of State, shall submit to the appropriate congressional committees a report on\u2014\n**(1)**\nthe actions taken to carry out this section, including\u2014\n**(A)**\nthe number of foreign persons added to or removed from the list required by subsection (a) during the year preceding each such report, the dates on which such persons were so added or removed, and the reasons for so adding or removing such persons; and\n**(B)**\nan analysis that compares increases or decreases in the number of such persons added or removed year-over-year and the reasons therefore;\n**(2)**\nany efforts by the President to coordinate with the governments of other countries, as appropriate, to impose sanctions that are similar to the sanctions imposed under this section;\n**(3)**\nthe impact of the sanctions imposed under this section with respect to altering the behavior of each of the foreign persons included, as of the date of submission of the report, in the list required by subsection (a); and\n**(4)**\nsteps the Department can take to improve coordination with foreign governments, civil society groups, and the private sector, to prevent the commission of the human rights violations described in section 3(a)(1) against persons based on actual or perceived sexual orientation, gender identity, or sex characteristics.\n##### (g) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services, the Committee on Foreign Affairs, the Committee on Homeland Security, and the Committee on the Judiciary of the House of Representatives; and\n**(B)**\nthe Committee on Armed Services, the Committee on Foreign Relations, the Committee on Homeland Security and Governmental Affairs, and the Committee on the Judiciary of the Senate.\n**(2) Foreign person**\nThe term foreign person has the meaning given such term in section 595.304 of title 31, Code of Federal Regulations (as in effect on the day before the date of enactment of this Act).\n**(3) Immediate family member**\nThe term immediate family member has the meaning given such term for purposes of section 7031(c) of division K of the Consolidated Appropriations Act, 2021.\n**(4) Person**\nThe term person has the meaning given such term in section 591.308 of title 31, Code of Federal Regulations (as in effect on the day before the date of enactment of this Act).\n#### 5. Combating international criminalization of lgbtqi status, expression, or conduct\n##### (a) Annual strategic review\nThe Secretary of State, in consultation with the Administrator of the United States Agency for International Development, shall include during the course of annual strategic planning an examination of the progress made in countries around the world toward the decriminalization of the status, expression, and conduct of LGBTQI individuals, the obstacles that remain toward achieving such decriminalization, and the strategies available to the Department and the Agency to address such obstacles.\n##### (b) Elements\nThe examination described in subsection (a) shall include the following:\n**(1)**\nAn examination of the full range of criminal and civil laws of other countries that disproportionately impact communities of LGBTQI individuals or apply with respect to the conduct of LGBTQI individuals.\n**(2)**\nIn consultation with the Attorney General, a list of countries in each geographic region with respect to which\u2014\n**(A)**\nthe Attorney General, acting through the Office of Overseas Prosecutorial Development Assistance and Training of the Department of Justice, shall prioritize programs seeking to\u2014\n**(i)**\ndecriminalize the status, expression, and conduct of LGBTQI individuals;\n**(ii)**\nmonitor the trials of those prosecuted because of such status, expression, or conduct; and\n**(iii)**\nreform related laws having a discriminatory impact on LGBTQI individuals; and\n**(B)**\napplicable speaker or exchange programs sponsored by the United States Government shall bring together civil society and governmental leaders to promote the recognition of LGBTQI rights through educational exchanges in the United States and support better understanding of the role that governments and civil societies mutually play in assurance of equal treatment of LGBTQI populations abroad.\n#### 6. Foreign assistance to protect human rights of lgbtqi people\n##### (a) Sense of congress\nIt is the sense of Congress that the full implementation of Executive Order 13988 and Bostock requires that United States foreign assistance and development organizations adopt the policy that no contractor, grantee, or implementing partner administering United States assistance for any humanitarian, development, or global health programs may discriminate against any employee or applicant for employment because of their gender identity or sexual orientation.\n##### (b) Global equality fund\n**(1) In general**\nThe Secretary of State shall establish a fund, to be known as the Global Equality Fund , to be managed by the Assistant Secretary of the Bureau of Democracy, Human Rights and Labor, consisting of such sums as may be appropriated to provide grants, emergency assistance, and technical assistance to eligible civil society organizations and human rights defenders working to advance and protect human rights for all including LGBTQI persons, by seeking to achieve the following:\n**(A)**\nEnsuring the freedoms of assembly, association, and expression.\n**(B)**\nProtecting persons or groups against the threat of violence, including medically unnecessary interventions performed on intersex infants.\n**(C)**\nAdvocating against laws that criminalize LGBTQI status, expression, or conduct or discriminate against individuals on the basis of sexual orientation, gender identity, or sex characteristics.\n**(D)**\nEnding explicit and implicit forms of discrimination in the workplace, housing, education, and other public institutions or services.\n**(E)**\nBuilding community awareness and support for the human rights of LGBTQI persons.\n**(2) Contributions**\nThe Secretary may accept financial and technical contributions from corporations, bilateral donors, foundations, nongovernmental organizations, and other entities supporting the outcomes described in paragraph (1), through the Global Equality Fund.\n**(3) Prioritization**\nIn providing assistance through the Global Equality Fund, the Secretary shall ensure due consideration and appropriate prioritization of assistance to groups that have historically been excluded from programs undertaken for the outcomes described in paragraph (1).\n##### (c) LGBTQI global development partnership\nThe Administrator of the United States Agency for International Development, in consultation with the Secretary of State, shall establish a partnership, to be known as the LGBTQI Global Development Partnership , to leverage the financial and technical contributions of corporations, bilateral donors, foundations, nongovernmental organizations, and universities to support the human rights and development of LGBTQI persons around the world by supporting programs, projects, and activities for the following purposes:\n**(1)**\nTo strengthen the capacity of LGBTQI leaders and civil society organizations.\n**(2)**\nTo train LGBTQI leaders to effectively participate in democratic processes and lead civil institutions.\n**(3)**\nTo conduct research to inform national, regional, or global policies and programs.\n**(4)**\nTo promote inclusive development, including economic empowerment through enhanced LGBTQI entrepreneurship and business development.\n##### (d) Consultation\nIn coordinating programs, projects, and activities through the Global Equality Fund or the Global Development Partnership, the Secretary of State shall consult, as appropriate, with the Administrator of the United States Agency for International Development and the heads of other relevant Federal departments and agencies.\n##### (e) Report\nThe Secretary of State shall submit to the appropriate congressional committees an annual report on the work of, successes obtained, and challenges faced by the Global Equality Fund and the LGBTQI Global Development Partnership established in accordance with this section.\n##### (f) Limitation on assistance relating to equal access\n**(1) In general**\nNone of the amounts authorized to be appropriated or otherwise made available to provide United States assistance for any humanitarian, development, or global health programs may be made available to any contractor, grantee, or implementing partner, unless such recipient\u2014\n**(A)**\nensures that the program, project, or activity funded by such amounts are made available to all elements of the population, except to the extent that such program, project, or activity targets a population because of the higher assessed risk of negative outcomes among such populations;\n**(B)**\nundertakes to make every reasonable effort to ensure that each subcontractor or subgrantee of such recipient will also adhere to the requirement described in subparagraph (A); and\n**(C)**\nagrees to return all amounts awarded or otherwise provided by the United States, including such additional penalties as the Secretary of State may determine to be appropriate, if the recipient is not able to adhere to the requirement described in subparagraph (A).\n**(2) Quarterly report**\nThe Secretary of State shall provide to the appropriate congressional committees a quarterly report on the methods by which the Department monitors compliance with the requirement in paragraph (1)(A).\n##### (g) Office of foreign assistance\nThe Secretary of State, acting through the Director of the Office of Foreign Assistance, shall monitor the amount of foreign assistance obligated and expended on programs, projects, and activities relating to LGBTQI people, and shall provide the results of the indicators tracking such expenditure, upon request, to the Organization for Economic Co-operation and Development.\n#### 7. Global health inclusivity\n##### (a) In general\nThe Coordinator of United States Government Activities to Combat HIV/AIDS Globally shall develop mechanisms to ensure that the President\u2019s Emergency Plan for AIDS Relief (PEPFAR) is implemented in a way that equitably serves LGBTQI people in accordance with the goals described in section 6(f), including by requiring all partner entities receiving assistance through PEPFAR to receive training on the health needs of and human rights standards relating to LGBTQI people, and shall promptly notify Congress of any obstacles encountered by a foreign government or contractor, grantee, or implementing partner in the effort to equitably implement PEPFAR as described in such subsection, including any remedial steps taken by the Coordinator to overcome such obstacles.\n##### (b) Report on international prosecutions for sex work or consensual sexual activity\nNot later than 180 days after the date of enactment of this Act, the Coordinator shall submit to the appropriate congressional committees a report describing the manner in which commodities such as condoms provided by programs, projects, or activities funded through PEPFAR or other sources of United States assistance have been used as evidence to arrest, detain, or prosecute individuals in other countries in order to enforce domestic laws criminalizing sex work or consensual sexual activity.\n##### (c) Report on hiv/AIDS-Related index testing\nNot later than 180 days after the date of enactment of this Act, the Coordinator shall submit to the appropriate congressional committees a report describing the impact of partner notification services and index testing on treatment adherence, intimate partner violence, and exposure to the criminal justice system for key populations, including LGBTQI people and sex workers, using qualitative and quantitative data.\n##### (d) Report on impact of global gag rule\nNot later than 180 days after the date of enactment of this Act, the Comptroller General shall submit to the appropriate congressional committees a report describing the impact, as of the date of the submission of the report, on the implementation and enforcement of any iteration of the Mexico City Policy on the global LGBTQI community.\n##### (e) Removing limitations on eligibility for foreign assistance\n**(1) In general**\nNotwithstanding any other provision of law, regulation, or policy, in determining eligibility for assistance authorized under part I of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ), foreign nongovernmental organizations\u2014\n**(A)**\nshall not be ineligible for such assistance solely on the basis of health or medical services, including counseling and referral services, provided by such organizations with non-United States Government funds if such services do not violate the laws of the country in which they are being provided; and\n**(B)**\nshall not be subject to requirements relating to the use of non-United States Government funds for advocacy and lobbying activities other than those that apply to United States nongovernmental organizations receiving assistance under part I of such Act.\n**(2) Conforming amendments to pepfar authorization**\nSection 301 of the United States Leadership Against HIV/AIDS, Tuberculosis, and Malaria Act of 2003 ( 22 U.S.C. 7631 ) is amended\u2014\n**(A)**\nby striking subsections (d) through (f); and\n**(B)**\nby redesignating subsection (g) as subsection (d).\n**(3) Conforming amendments to the allocation of funds by the global aids coordinator**\nSection 403(a) of the United States Leadership Against HIV/AIDS, Tuberculosis, and Malaria Act of 2003 ( 22 U.S.C. 7673(a) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking shall\u2014 and all that follows through (A) provide and inserting shall provide ;\n**(ii)**\nby striking ; and and inserting a period; and\n**(iii)**\nby striking subparagraph (B); and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking Prevention strategy .\u2014 and all that follows through In carrying out paragraph (1) and inserting Prevention strategy .\u2014In carrying out paragraph (1) ; and\n**(ii)**\nby striking subparagraph (B).\n**(4) Conforming amendments to tvpra authorization**\nSection 113 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7110 ) is amended\u2014\n**(A)**\nby striking subsection (g); and\n**(B)**\nby redesignating subsections (h) and (i) as subsections (g) and (h), respectively.\n#### 8. Immigration reform\n##### (a) Refugees and asylum seekers\n**(1) LGBTQI social group**\nSection 101(a)(42) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(42) ) is amended by inserting after the period at the end the following: For purposes of determinations under this Act, a person who has been persecuted on the basis of sexual orientation or gender identity, shall be deemed to have been persecuted on account of membership in a particular social group, and a person who has a well founded fear of persecution on the basis of sexual orientation or gender identity shall be deemed to have a well founded fear of persecution on account of membership in a particular social group. .\n**(2) Report**\nSection 103(e) of the Immigration and Nationality Act ( 8 U.S.C. 1103(e) ) is amended by adding at the end the following:\n(3) Each annual report shall include information on the total number of applications for asylum and refugee status received that are, in whole or in part, based on persecution or a well founded fear of persecution on account of sexual orientation or gender identity, and the rate of approval administratively of such applications. .\n**(3) Asylum filing deadline repeal**\n**(A) In general**\nSection 208(a)(2)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a)(2)(B) ) is repealed.\n**(B) Conforming amendments**\nSection 208(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a)(2) ) is amended\u2014\n**(i)**\nin subparagraph (D)\u2014\n**(I)**\nby striking notwithstanding subparagraphs (B) and (C) and inserting notwithstanding subparagraph (C) ;\n**(II)**\nby striking either after Attorney General ; and\n**(III)**\nby striking or extraordinary circumstances relating to the delay in filing an application within the period specified in subparagraph (B) ; and\n**(ii)**\nin subparagraph (E), by striking Subparagraphs (A) and (B) and inserting Subparagraph (A) .\n**(C) Application**\nThe amendments made by this paragraph shall apply to applications for asylum filed before, on, or after the date of enactment of this Act.\n##### (b) Permanent partners\nSection 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ) is amended\u2014\n**(1)**\nin paragraph (35), by inserting includes any permanent partner, but before does not include ; and\n**(2)**\nby adding at the end the following:\n(53) The term marriage includes a permanent partnership. (54) The term permanent partner means an individual 18 years of age or older who\u2014 (A) is in a committed, intimate relationship with another individual 18 years of age or older, in which both parties intend a lifelong commitment; (B) is financially interdependent with the other individual; (C) is not married to anyone other than the other individual; (D) is a national of or, in the case of a person having no nationality, last habitually resided in a country that prohibits marriage between the individuals; and (E) is not a first-, second-, or third-degree blood relation of the other individual. (55) The term permanent partnership means the relationship that exists between 2 permanent partners. .\n##### (c) Counsel\n**(1) Appointment of counsel**\nSection 240(b)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(4) ) is amended\u2014\n**(A)**\nin subparagraph (B), by striking and at the end;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting , and ; and\n**(C)**\nby adding at the end the following:\n(D) notwithstanding subparagraph (A), in a case in which an indigent alien requests representation, such representation shall be appointed by the court, at the expense of the Government, for such proceedings. .\n**(2) Right to counsel**\nSection 292 of the Immigration and Nationality Act ( 8 U.S.C. 1362 ) is amended\u2014\n**(A)**\nby inserting (a) before In any ;\n**(B)**\nby striking he and inserting the person ; and\n**(C)**\nby adding at the end the following:\n(b) Notwithstanding subsection (a), in a case in which an indigent alien requests representation, such representation shall be appointed by the court, at the expense of the Government, for the proceedings described in subsection (a). (c) In an interview relating to admission under section 207, an alien shall have the privilege of being represented, at no expense to the Government, by such counsel, authorized to practice in such proceedings, as the alien shall choose. .\n##### (d) Refugee admissions of LGBTQI aliens from certain countries\n**(1) In general**\nIn the case of aliens who are nationals of or, in the case of aliens having no nationality, last habitually resided in a country that fails to protect against persecution on the basis of sexual orientation or gender identity and who share common characteristics that identify them as targets of persecution on account of sexual orientation or gender identity, such aliens are eligible for Priority 2 processing under the refugee resettlement priority system.\n**(2) Resettlement processing**\n**(A) In general**\nIn a case in which a refugee admitted under section 207 of the Immigration and Nationality Act discloses to an employee or contractor of the Bureau of Population, Refugees, and Migration information with respect to the refugee\u2019s sexual orientation or gender identity, the Secretary of State shall, with the refugee\u2019s consent, provide such information to the appropriate national resettlement agency to prevent the refugee from being placed in a community in which the refugee is likely to face continued discrimination and to place the refugee in a community that offers services to meet the needs of the refugee.\n**(B) National resettlement agencies defined**\nThe term national resettlement agency means an agency contracting with the Department of State to provide sponsorship and initial resettlement services to refugees entering the United States.\n##### (e) Training program\n**(1) Training program**\nIn order to create an environment in which an alien may safely disclose such alien\u2019s sexual orientation or gender identity, the Secretary of Homeland Security shall establish, in consultation with the Secretary of State, a training program for staff and translators who participate in the interview process of aliens seeking asylum or status as a refugee.\n**(2) Components of training program**\nThe training program described in paragraph (1) shall include instruction on\u2014\n**(A)**\nappropriate word choice and word usage;\n**(B)**\ncreating safe spaces and facilities for LGBTQI aliens;\n**(C)**\nconfidentiality requirements; and\n**(D)**\nnondiscrimination policies.\n##### (f) Limitation on detention\n**(1) Presumption of release**\n**(A) In general**\nNotwithstanding any other provision of law and except as provided in subparagraphs (B) and (C), the Secretary of Homeland Security\u2014\n**(i)**\nmay not detain an alien who is a member of a vulnerable group under any provision of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) pending a decision with respect to whether the alien is to be removed from the United States; and\n**(ii)**\nshall immediately release any detained alien who is a member of a vulnerable group.\n**(B) Exceptions**\nThe Secretary of Homeland Security may detain, pursuant to the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ), an alien who is a member of a vulnerable group if the Secretary makes a determination, using credible and individualized information, that the use of alternatives to detention will not reasonably assure the appearance of the alien at removal proceedings, or that the alien is a threat to another person or the community. The fact that an alien has a criminal charge pending against the alien may not be the sole factor to justify the detention of the alien.\n**(C) Removal**\nIn a case in which detention is the least restrictive means of effectuating the removal from the United States of an alien who is a member of a vulnerable group, the subject of a final order of deportation or removal, and not detained under subparagraph (B), the Secretary of Homeland Security may, solely for the purpose of such removal, detain the alien for a period that is\u2014\n**(i)**\nthe shortest possible period immediately preceding the removal of the alien from the United States; and\n**(ii)**\nnot more than 5 days.\n**(2) Weekly review required**\n**(A) In general**\nWith respect to an alien detained under subparagraph (B) of paragraph (1), not less frequently than once each week, the Secretary of Homeland Security shall conduct an individualized review to determine whether the alien should continue to be detained under such subparagraph.\n**(B) Release**\nIn the case of a determination under subparagraph (A) that an alien should not be detained under paragraph (1)(B), not later than 24 hours after the date on which the Secretary makes the determination, the Secretary shall release the detainee.\n##### (g) Protective custody for LGBTQI alien detainees\n**(1) Detainees**\nAn LGBTQI alien who is detained under subparagraph (B) or (C) of subsection (f)(1) may not be placed in housing that is segregated from the general population unless\u2014\n**(A)**\nthe alien requests placement in such housing for the protection of the alien; or\n**(B)**\nthe Secretary of Homeland Security determines, after assessing all available alternatives, that there is no available alternative means of separation from likely abusers.\n**(2) Placement factors**\nIn a case in which an LGBTQI alien is placed in segregated housing pursuant to paragraph (1), the Secretary of Homeland Security shall ensure that such housing\u2014\n**(A)**\nincludes non-LGBTQI aliens, to the extent practicable; and\n**(B)**\ncomplies with any applicable court order for the protection of LGBTQI aliens.\n**(3) Protective custody requests**\nIn a case in which an LGBTQI alien who is detained requests placement in segregated housing for the protection of such alien, the Secretary of Homeland Security shall grant such request.\n##### (h) Sense of congress\nIt is the sense of Congress that the Secretary of Homeland Security should hire a sufficient number of Refugee Corps officers for refugee interviews to be held within a reasonable period of time and adjudicated not later than 180 days after a request for Priority 2 consideration is filed.\n#### 9. Issuance of passports and guarantee of citizenship to certain children born abroad\n##### (a) Sex identification markers\nFor the purposes of any identity document issued by the Department that displays sex information, including passports and consular reports of birth abroad, the Secretary shall ensure (through appropriate regulation, manual, policy, form, or other updates) that an applicant for such a document may self-select the sex designation, including a nonbinary or neutral designation (such as X ).\n##### (b) Guarantee of citizenship to children born abroad using assistive reproduction technology\nNot later than 90 days after the date of enactment of this Act, the Secretary of State shall issue regulations, in accordance with the press statement released on May 18, 2021, with respect to U.S. Citizenship Transmission and Assisted Reproductive Technology , clarifying that no biological connection between a parent and a child is required for a child to acquire citizenship at birth from a United States citizen parent under sections 301(c), (d), (e), and (g) of the Immigration and Nationality Act ( 8 U.S.C. 1401(c) , (d), (e), and (g)), provided that either the local law at the place of birth or United States law recognize such a person to be the legal parent of the child from birth.\n#### 10. Engaging international organizations in the fight against lgbtqi discrimination\n##### (a) Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States should be a leader in efforts by the United Nations to ensure that human rights norms, development principles, and political rights are fully inclusive of LGBTQI people;\n**(2)**\nUnited States leadership within international financial institutions, such as the World Bank and the regional development banks, should be used to ensure that the programs, projects, and activities undertaken by such institutions are fully inclusive of all people, including LGBTQI people; and\n**(3)**\nthe Secretary of State should seek appropriate opportunities to encourage the equal treatment of LGBTQI people during discussions with or participation in the full range of regional, multilateral, and international fora, such as the Organization of American States, the Organization for Security and Cooperation in Europe, the European Union, the African Union, and the Association of South East Asian Nations.\n##### (b) Action through the equal rights coalition\nThe Secretary of State shall promote diplomatic coordination through the Equal Rights Coalition, established in July 2016 at the Global LGBTQI Human Rights Conference in Montevideo, Uruguay, and other multilateral mechanisms, to achieve the goals and outcomes described in subsection (a).\n#### 11. Representing the rights of united states lgbtqi citizens deployed to diplomatic and consular posts\n##### (a) Sense of congress\nIt is the sense of Congress that, recognizing the importance of a diverse workforce in the representation of the United States abroad, and in support of sound personnel staffing policies, the Secretary of State should\u2014\n**(1)**\nprioritize efforts to ensure that foreign governments do not impede the assignment of United States LGBTQI citizens and their families to diplomatic and consular posts;\n**(2)**\nopen conversations with entities in the United States private sector that engage in business in other countries to the extent necessary to address any visa issues faced by such private sector entities with respect to their LGBTQI employees; and\n**(3)**\nprioritize efforts to improve post and post school information for LGBTQI employees and employees with LGBTQI family members.\n##### (b) Remedies for family visa denial\n**(1) In general**\nThe Secretary of State shall use all appropriate diplomatic efforts to ensure that the families of LGBTQI employees of the Department are issued visas from countries where such employees are posted.\n**(2) List required**\nNot later than 180 days after the date of enactment of this Act, the Secretary of State shall submit to Congress\u2014\n**(A)**\na classified list of each country that has refused to grant accreditation to LGBTQI employees of the Department or their family members in the prior 2 years; and\n**(B)**\nthe actions taken or intended to be taken by the Secretary, in accordance with paragraph (1), to ensure that LGBTQI employees are appointed to appropriate positions in accordance with diplomatic needs and personnel qualifications, including actions specifically relating to securing the accreditation of the families of such employees by relevant countries.\n##### (c) Improving post information and overseas environment for LGBTQI adults and children\n**(1) In general**\nThe Secretary of State shall ensure that LGBTQI employees and employees with LGBTQI family members have adequate information to pursue overseas postings, including country environment information for adults and children.\n**(2) Non-discrimination policies for united states government-supported schools**\nThe Secretary shall make every effort to ensure schools abroad that receive assistance and support from the United States Government under programs administered by the Office of Overseas Schools of the Department of State have active and clear nondiscrimination policies, including policies relating to sexual orientation and gender identity impacting LGBTQI children of all ages.\n**(3) Required information for LGBTQI children**\nThe Secretary shall ensure that information focused on LGBTQI children of all ages (including transgender and gender nonconforming students) is included in post reports, bidding materials, and Office of Overseas Schools reports, databases, and adequacy lists.\n#### 12. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs, the Committee on the Judiciary, and the Committee on Appropriations of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations, the Committee on the Judiciary, and the Committee on Appropriations of the Senate.\n**(2) Gender identity**\nThe term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth.\n**(3) LGBTQI**\nThe term LGBTQI means lesbian, gay, bisexual, transgender, queer, or intersex.\n**(4) Member of a vulnerable group**\nThe term member of a vulnerable group means, with respect to an alien, that such alien\u2014\n**(A)**\nis under 21 years of age or over 60 years of age;\n**(B)**\nis pregnant;\n**(C)**\nidentifies as lesbian, gay, bisexual, transgender, or intersex;\n**(D)**\nis a victim or witness of a crime;\n**(E)**\nhas filed a nonfrivolous civil rights claim in Federal or State court;\n**(F)**\nhas a serious mental or physical illness or disability;\n**(G)**\nhas been determined by an asylum officer in an interview conducted under section 235(b)(1)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(1)(B) ) to have a credible fear of persecution; or\n**(H)**\nhas been determined by an immigration judge or the Secretary of Homeland Security to be experiencing severe trauma or to be a survivor of torture or gender-based violence, based on information obtained during intake, from the alien\u2019s attorney or legal service provider, or through credible self-reporting.\n**(5) Sexual orientation**\nThe term sexual orientation means actual or perceived homosexuality, heterosexuality, or bisexuality.",
      "versionDate": "2025-06-27",
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
        "actionDate": "2025-07-09",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "2231",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GLOBE Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-07-29T21:48:30Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4245ih.xml"
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
      "title": "GLOBE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:10Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GLOBE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Greater Leadership Overseas for the Benefit of Equality Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect human rights and enhance opportunities for LGBTQI people around the world, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T04:18:26Z"
    }
  ]
}
```
