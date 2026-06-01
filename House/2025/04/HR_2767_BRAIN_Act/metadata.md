# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2767?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2767
- Title: BRAIN Act
- Congress: 119
- Bill type: HR
- Bill number: 2767
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-05-30T08:05:36Z
- Update date including text: 2026-05-30T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2767",
    "number": "2767",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "BRAIN Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:36Z",
    "updateDateIncludingText": "2026-05-30T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MA"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "WA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
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
      "sponsorshipDate": "2025-04-30",
      "state": "KS"
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
      "sponsorshipDate": "2025-05-06",
      "state": "DC"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "IL"
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
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
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
      "sponsorshipDate": "2025-05-19",
      "state": "DE"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
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
      "sponsorshipDate": "2025-05-21",
      "state": "MD"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NJ"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "TN"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "IL"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-09",
      "state": "VA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "MP"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CO"
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
      "sponsorshipDate": "2025-08-08",
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
      "sponsorshipDate": "2025-08-22",
      "state": "MD"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-11",
      "state": "WA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "RI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CO"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
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
      "sponsorshipDate": "2025-10-14",
      "state": "NC"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "FL"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NE"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "ME"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NJ"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "WA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
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
      "sponsorshipDate": "2026-05-26",
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
      "sponsorshipDate": "2026-05-29",
      "state": "AZ"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2767ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2767\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Fitzpatrick (for himself, Mrs. Trahan , Mr. Joyce of Pennsylvania , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo advance research to achieve medical breakthroughs in brain tumor treatment and improve awareness and adequacy of specialized cancer and brain tumor care.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Bolstering Research And Innovation Now Act or the BRAIN Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings; purposes.\nSec. 3. Fostering transparency of biospecimen collections for brain cancer research.\nSec. 4. Glioblastoma Therapeutics Network; brain tumor related cellular immunotherapy (including CAR\u2013T) team science award.\nSec. 5. Cancer clinical trials and biomarker testing national public awareness campaign.\nSec. 6. Pilot programs to develop, study, or evaluate approaches to monitoring and caring for brain tumor survivors.\nSec. 7. FDA guidance to ensure brain tumor patient access to clinical trials.\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds as follows:\n**(1)**\nAccording to the National Brain Tumor Society based on data analyzed in 2024, more than 1,000,000 people in the United States are living with a brain tumor and approximately 94,000 were estimated to be diagnosed with a primary brain tumor in 2023.\n**(2)**\nBrain tumors do not discriminate and can affect people of all races, genders, and ages. Tragically, pediatric brain tumors are the leading cause of cancer-related death among children and young adults ages 19 and younger.\n**(3)**\nFor malignant brain tumors, incidence and survival rates have remained stagnant for 45 years, with an average 5-year relative survival rate of 35.7 percent and only 6.9 percent for glioblastoma, the most common primary malignant brain tumor.\n**(4)**\nMost primary brain tumors are non-malignant, but many still require surgery and radiation. The results of available treatment options can vary from a successful return to normal life to possible disability or a life-threatening condition.\n**(5)**\nDespite the statistics described in paragraphs (1) through (4), there have been very few treatments ever approved by the Food and Drug Administration to treat brain tumors, thereby resulting in little change in mortality rates for individuals with brain tumors.\n**(6)**\nAs of the date of enactment of this Act, there is no prevention and no early detection protocol for brain tumors.\n**(7)**\nAll people in the United States have a stake in reducing and eliminating brain tumors.\n**(8)**\nPatients living with a brain tumor and their families want cures. Short of cures, they want safe and effective ways to increase survival rates for such patients and improve the quality of life for such patients.\n##### (b) Purposes\nThe purposes of this Act are to\u2014\n**(1)**\nstrengthen research and treatment development regarding brain tumors; and\n**(2)**\nimprove the adequacy and awareness of, and access to, specialized brain tumor, and rare and recalcitrant cancer, health care.\n#### 3. Fostering transparency of biospecimen collections for brain cancer research\nPart A of title IV of the Public Health Service Act ( 42 U.S.C. 281 et seq. ) is amended by adding at the end the following:\n404P. Reporting of brain tumor biospecimen collections (a) Definition of covered biospecimen collection (1) In general In this section, the term covered biospecimen collection means a biospecimen that was collected or acquired in whole or in part through funding from the National Institutes of Health. (2) Biospecimen For purposes of paragraph (1), the term biospecimen means a brain tumor tissue, cerebral spinal fluid, or other specimen type listed by the Specimen Resource Locator of the National Cancer Institute (or a successor database). (b) Establishment The Secretary, acting through the Director of NIH, may establish and maintain a searchable website, or multiple websites, which may include websites existing on the day before the date of enactment of this section, for the purpose of making accessible to the public\u2014 (1) information on the existence and location of covered biospecimen collections; (2) a description of such collections; and (3) contact information with respect to such collections. (c) Reporting requirements (1) Existing collections Any individual or entity that as of the date of enactment of this section maintains a covered biospecimen collection shall, not later than 180 days after such date of enactment, submit a report to the Director of NIH containing information with respect to such covered biospecimen collection as the Director of NIH may specify, including at a minimum the information the National Cancer Institute requires for the Specimen Resource Locator (or a successor database). (2) New collections Any individual or entity that collects or acquires a covered biospecimen collection on or after the date of enactment of this section shall, not later than 60 days after the date of such collection or acquisition, submit a report to the Director of NIH containing the information required under paragraph (1). (d) Oversight The Secretary, acting through the Director of NIH, shall establish and carry out an oversight mechanism, which shall include withholding funding to individuals or entities that have committed a repeated or egregious violation of the requirements under subsection (c). .\n#### 4. Glioblastoma Therapeutics Network; brain tumor related cellular immunotherapy (including CAR\u2013T) team science award\n##### (a) In general\nSubpart 1 of part C of title IV of the Public Health Service Act ( 42 U.S.C. 285 et seq. ) is amended by adding at the end the following:\n417H. Glioblastoma Therapeutics Network (a) In general The Director of the Institute shall carry out a research program, known as the Glioblastoma Therapeutics Network , by awarding, on a competitive basis, cooperative agreements, or other awards, through the U19 funding mechanism of the National Institutes of Health for collaboration of institutions to improve the treatment of glioblastoma by evaluating therapeutic agents from pre-clinical development studies through completion of early-phase clinical trials in humans. (b) Authorization of appropriations There is authorized to be appropriated $50,000,000 for each of fiscal years 2026 through 2030, to remain available until expended, to the Director of the Institute to carry out this section. 417I. Brain tumor related cellular immunotherapy (including CAR\u2013T) team science award (a) In general (b) In order to take advantage of the significant advancement in the development of brain tumor related cellular immunotherapy, including chimeric antigen receptor\u2013T (in this section referred to as CAR\u2013T ), including many such approaches previously funded by the National Institutes of Health, the Director of the Institute shall make awards, on a competitive basis, through a U series funding mechanism, to support the development of a multi-institutional team science approach to using brain tumor related cancer cellular immunotherapy, including CAR\u2013T treatment, for adult and pediatric brain tumors. (b) Use of funds Funds received through an award under this section shall be used\u2014 (1) to support collaborative, multi-institutional research activities, including pre-clinical and investigational new drug studies; and (2) for the purpose of supporting clinical trials to evaluate brain tumor related cancer cellular immunotherapy, including CAR\u2013T. (c) Authorization of appropriations There is authorized to be appropriated $10,000,000 for each of fiscal years 2026 through 2030, to remain available until expended, to the Director of the Institute to carry out this section. .\n##### (b) Transition for the Glioblastoma Therapeutics Network\nThe Director of the National Cancer Institute shall take such steps as may be necessary for the orderly transition from the Glioblastoma Therapeutics Network carried out by the Director, as of the day before the date of enactment of this Act, to the research program authorized under section 417H of the Public Health Service Act, as added by subsection (a). In making such transition, the Director shall ensure that the program authorized under such section 417H is based upon and consistent with the policies and procedures of the Glioblastoma Therapeutics Network carried out by the Director as of the day before the date of enactment of this Act.\n#### 5. Cancer clinical trials and biomarker testing national public awareness campaign\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Cancer clinical trials and biomarker testing national public awareness campaign (a) National campaign (1) In general The Secretary shall carry out a national campaign to increase the awareness and knowledge of health care providers and individuals, including patients and caregivers, with respect to the importance of clinical trials in the treatment of cancer. (2) Activities (A) In general Activities under such national campaign shall include each of the following: (i) Written materials Maintaining a supply of written and digital materials that provide information to the public on clinical trials, and distributing such materials to members of the public upon request. (ii) Public service announcements; public engagement Providing public service announcements, in accordance with applicable law, including through publishing materials in digital or print form, and carrying out other public engagement initiatives. Such public service announcements and other public engagement initiatives shall include such announcements and initiatives intended to encourage individuals to discuss with their physicians\u2014 (I) what cancer clinical trials are; (II) the importance of clinical trials in the treatment of cancer; (III) how to enroll in cancer clinical trials; (IV) what cancer biomarker testing is; (V) the importance of biomarker testing in the diagnosis and treatment of cancer; and (VI) how to access cancer biomarker testing. (B) Targeted populations The Secretary shall ensure that the national campaign includes communications, including public service announcements and other public engagement initiatives under subparagraph (A)(ii), that are\u2014 (i) culturally and linguistically competent; and (ii) targeted to\u2014 (I) specific populations that are at a higher risk of cancer, including such populations based on factors including race, ethnicity, level of acculturation, and family history; (II) rural communities; and (III) such other communities as the Secretary determines appropriate. (3) Consultation In carrying out the national campaign under this subsection, the Secretary shall consult with\u2014 (A) health care providers; (B) nonprofit organizations; (C) State and local public health departments; and (D) elementary and secondary schools and institutions of higher education. (b) Demonstration projects regarding outreach and education strategies for cancer and brain tumor patients (1) In general The Secretary shall carry out a program to award grants or contracts to public or nonprofit private entities for the purpose of carrying out demonstration projects to test, compare, and evaluate different evidence-based outreach and education strategies to increase the awareness and knowledge of cancer and brain tumor clinical trials and biomarker testing. Such projects shall focus on the awareness and knowledge of patients (and the families of patients), physicians, nurses, and other key health professionals involved in brain tumor treatment. (2) Awards In making awards under paragraph (1), the Secretary shall\u2014 (A) ensure that information provided through demonstration projects supported by such an award is consistent with the best available medical information; and (B) give preference to\u2014 (i) applicants with demonstrated expertise in\u2014 (I) biomarker testing and clinical trials in brain tumors and other recalcitrant cancers; (II) brain cancer and other recalcitrant cancer education or treatment; (III) working with groups of patients and caregivers; and (IV) reaching geographic areas that have historically low rates of participation in cancer clinical trials; and (ii) applicants that demonstrate in their application submitted under paragraph (3) that the project for which they are seeking a grant or contract will involve and connect physicians, nurses, other key health professionals, health profession students, hospitals, and payers. (3) Applications To seek a grant or contract under this subsection, an entity shall submit an application to the Secretary in such form, in such manner, and containing such agreements, assurances, and information as the Secretary may reasonably require. (c) Authorization of appropriations For the purpose of carrying out this section, there is authorized to be appropriated $10,000,000 for the period of fiscal years 2026 through 2030. .\n#### 6. Pilot programs to develop, study, or evaluate approaches to monitoring and caring for brain tumor survivors\nPart B of title IV of the Public Health Service Act ( 42 U.S.C. 284 et seq. ) is amended by adding at the end the following:\n409K. Pilot programs to develop, study, or evaluate approaches to monitoring and caring for brain tumor survivors (a) In general The Director of NIH may, as appropriate, make awards to eligible entities to establish pilot programs to develop, study, or evaluate approaches, including primary and specialty care, for monitoring and caring for adult and pediatric brain tumor survivors throughout their lifespan, including evaluating models for transition to post-treatment care and care coordination. (b) Awards (1) Eligible entities (A) In general For purposes of this section, an eligible entity is\u2014 (i) a medical school; (ii) a children\u2019s hospital; (iii) a cancer center; (iv) a community-based medical facility; or (v) any other entity with significant experience and expertise in carrying out the activities described in subsection (a). (B) Types of entities Awards under this section shall be made, to the extent practical, to\u2014 (i) small, medium, and large-sized eligible entities; and (ii) sites located in different geographic areas, including rural and urban areas. (2) Peer review In making awards under this section, the Director of NIH shall comply with the peer review requirements in section 492. (3) Use of funds Funds from awards under this section may be used to develop, study, or evaluate one or more models for monitoring and caring for brain tumor survivors, which may include\u2014 (A) evaluating follow-up care, educational accommodations, monitoring, and other survivorship programs (including peer support and mentoring programs); (B) developing and evaluating models for providing multidisciplinary care; (C) disseminating information to health care providers about culturally and linguistically appropriate follow-up care for brain tumor survivors and their families, as appropriate and practicable; (D) developing and evaluating existing psychosocial evaluations, counseling, and support programs to improve the quality of life of brain tumor survivors and their families, which may include peer support and mentoring programs; (E) designing and evaluating tools, which may include tools generated by artificial intelligence and machine learning, to support the secure electronic transfer of treatment information and care summaries from brain tumor care providers to other health care providers (including primary and specialty care providers), which information and care summaries shall include risk factors and a plan for recommended follow-up care; (F) developing and evaluating initiatives that promote the coordination and effective transition of care between brain tumor care providers, primary and specialty care providers, mental health professionals, and other health care professionals, as appropriate, including models that use a team-based or multi-disciplinary approach to care; and (G) disseminating information described in subparagraphs (A) through (F), including with respect to models, evaluations, programs, systems, and initiatives described in such subparagraphs, to other health care providers (including primary and specialty care providers) and to pediatric brain tumor survivors and their families, where appropriate and in accordance with Federal and State law. (c) Authorization of appropriations There are authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2026 through 2030. .\n#### 7. FDA guidance to ensure brain tumor patient access to clinical trials\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall issue guidance to help identify ways to minimize the potential for the exclusion of brain tumor patients and patients with rare and recalcitrant cancers from clinical trials evaluating treatments for other indications.",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-08",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1330",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "BRAIN Act",
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
        "name": "Health",
        "updateDate": "2025-05-19T14:53:53Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2767ih.xml"
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
      "title": "BRAIN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BRAIN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bolstering Research And Innovation Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To advance research to achieve medical breakthroughs in brain tumor treatment and improve awareness and adequacy of specialized cancer and brain tumor care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T04:48:25Z"
    }
  ]
}
```
