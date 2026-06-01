# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1822?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1822
- Title: ACRE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1822
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2025-12-19T09:07:35Z
- Update date including text: 2025-12-19T09:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1822",
    "number": "1822",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "ACRE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:35Z",
    "updateDateIncludingText": "2025-12-19T09:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:01:00Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OK"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "LA"
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
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "WI"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "SD"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "WI"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "WI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "UT"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "IA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "KY"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MO"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TN"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MO"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
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
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "IL"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "NE"
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
      "sponsorshipDate": "2025-04-24",
      "state": "NC"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NH"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-30",
      "state": "NJ"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "MN"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "ND"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "OR"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "GA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "UT"
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
      "sponsorshipDate": "2025-05-07",
      "state": "AL"
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
      "sponsorshipDate": "2025-05-07",
      "state": "GA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "DE"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "NY"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "WI"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AR"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AR"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "TX"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "OH"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
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
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1822ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1822\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Feenstra (for himself, Mr. Davis of North Carolina , and Mr. Moran ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income interest received on certain loans secured by rural or agricultural real property.\n#### 1. Short title\nThis Act may be cited as the Access to Credit for our Rural Economy Act of 2025 or the ACRE Act of 2025 .\n#### 2. Exclusion of interest on loans secured by rural or agricultural real property\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Interest on loans secured by rural or agricultural real property (a) In general Gross income shall not include interest received by a qualified lender on any qualified real estate loan. (b) Qualified lender For purposes of this section, the term qualified lender means\u2014 (1) any bank or savings association the deposits of which are insured under the Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ), (2) any State- or Federally-regulated insurance company, (3) any entity wholly owned, directly or indirectly, by a company that is treated as a bank holding company for purposes of section 8 of the International Banking Act of 1978 ( 12 U.S.C. 3106 ) if\u2014 (A) such entity is organized, incorporated, or established under the laws of the United States or any State of the United States, and (B) the principal place of business of such entity is in the United States (including any territory of the United States), (4) any entity wholly owned, directly or indirectly, by a company that is considered an insurance holding company under the laws of any State if such entity satisfies the requirements described in subparagraphs (A) and (B) of paragraph (3), and (5) with respect to interest received on a qualified real estate loan secured by real estate described in subsection (c)(3)(A), any federally chartered instrumentality of the United States established under section 8.1(a) of the Farm Credit Act of 1971 ( 12 U.S.C. 2279aa\u20131(a) ). (c) Qualified real estate loan For purposes of this section\u2014 (1) In general The term qualified real estate loan means any loan\u2014 (A) secured by\u2014 (i) rural or agricultural real estate or forestland, or (ii) a leasehold mortgage (with a status as a lien) on rural or agricultural real estate, (B) which is made to a person other than a foreign adversary entity, (C) in the case of any loan with respect to single family residence described in paragraph (3)(B)\u2014 (i) the proceeds of which are used to purchase or improve such residence, and (ii) the principal of which (when added to the principal of all other such loans with respect to such residence) does not (as of the time the interest income on such loan is accrued) exceed $750,000, and (D) made after the date of the enactment of this section. For purposes of the preceding sentence, the determination of whether property securing such loan is rural or agricultural real estate shall be made as of the time the interest income on such loan is accrued. (2) Refinancings For purposes of subparagraphs (A) and (C) of paragraph (1), a loan shall not be treated as made after the date of the enactment of this section to the extent that the proceeds of such loan are used to refinance a loan which was made on or before the date of the enactment of this Act (or, in the case of any series of refinancings, the original loan was made on or before such date). (3) Rural or agricultural real estate The term rural or agricultural real estate means\u2014 (A) any real property which is substantially used for the production of one or more agricultural products, (B) any single family residence\u2014 (i) which is the principal residence (within the meaning of section 121) of its occupant, and (ii) which is located in a rural area within the meaning of section 1.11(b)(3) of the Agricultural Credit Act of 1987 ( 12 U.S.C. 2019(b)(3) ), (C) any real property which is substantially used in the trade or business of fishing or seafood processing, and (D) any aquaculture facility. (4) Aquaculture facility The term aquaculture facility means any land, structure, or other appurtenance that is used for aquaculture (including any hatchery, rearing pond, raceway, pen, or incubator) that is located in any State or any territory of the United States. (5) Foreign adversary entity (A) In general The term foreign adversary entity means\u2014 (i) a foreign adversary, (ii) a foreign person subject to the jurisdiction of, or organized under the laws of, a foreign adversary, and (iii) a foreign person owned, directed, or controlled by an entity described in clause (i) or (ii). (B) Foreign adversary The term foreign adversary means\u2014 (i) the People\u2019s Republic of China, including all Special Administrative Regions, (ii) the Republic of Cuba, (iii) the Islamic Republic of Iran, (iv) the Democratic People\u2019s Republic of Korea, (v) the Russian Federation, and (vi) the Bolivarian Republic of Venezuela during any period of time in which Nichol\u00e1s Maduro is President of the Republic. (d) Coordination with section 265 Qualified real estate loans shall be treated as obligations described in section 265(a)(2) the interest on which is wholly exempt from the taxes imposed by this subtitle. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Interest on loans secured by rural or agricultural real property. .\n##### (c) Report to Congress\nNot later than 5 years after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall submit a written report to the Committee on Ways and Means of House of Representatives and the Committee on Finance of the Senate analyzing the impact of section 139J of the Internal Revenue Code of 1986 (as added by subsection (a)) on qualified real estate loans (as defined in such section), including whether such section has resulted in a reduction in the rate of interest on such loans.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-03-04",
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
        "actionDate": "2025-03-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ACRE Act of 2025",
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
        "updateDate": "2025-05-09T14:57:02Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1822ih.xml"
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
      "title": "ACRE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T08:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACRE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to Credit for our Rural Economy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude from gross income interest received on certain loans secured by rural or agricultural real property.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T08:48:20Z"
    }
  ]
}
```
