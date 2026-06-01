# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2398
- Title: Rural Veterinary Workforce Act
- Congress: 119
- Bill type: HR
- Bill number: 2398
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-04-15T08:05:50Z
- Update date including text: 2026-04-15T08:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2398",
    "number": "2398",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Rural Veterinary Workforce Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:50Z",
    "updateDateIncludingText": "2026-04-15T08:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:07:50Z",
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
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "IA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "NM"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "PA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MS"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
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
      "sponsorshipDate": "2025-04-02",
      "state": "AL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
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
      "sponsorshipDate": "2025-04-09",
      "state": "KS"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "KS"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "WV"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
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
      "sponsorshipDate": "2025-06-12",
      "state": "DC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WI"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "WA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NM"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "TN"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "IL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "MI"
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
      "sponsorshipDate": "2025-07-22",
      "state": "WA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "PR"
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
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "ID"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "IN"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "MD"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NH"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-18",
      "state": "MI"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "RI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "IL"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "KS"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NH"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "IN"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "IN"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WI"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DE"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CO"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "ME"
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
      "sponsorshipDate": "2026-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MO"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2398ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2398\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Smith of Nebraska (for himself, Mr. Larson of Connecticut , Mrs. Fischbach , Mr. Panetta , Mr. Feenstra , Ms. Stansbury , Mr. Rouzer , Mr. Carey , Ms. Budzinski , Ms. Houlahan , Mr. Davis of North Carolina , Mr. Kelly of Mississippi , Mr. Finstad , and Ms. McCollum ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for an exclusion for assistance provided to participants in certain veterinary student loan repayment or forgiveness programs.\n#### 1. Short title\nThis Act may be cited as the Rural Veterinary Workforce Act .\n#### 2. Exclusion for assistance provided to participants in certain veterinary student loan repayment or forgiveness programs\n##### (a) In general\nSection 108(f)(4) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking or after such Act, ;\n**(2)**\nby striking the period at the end and inserting , under section 1415A of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3151a ), or under any other State loan repayment or loan forgiveness program that is intended to provide for increased access to veterinary services in such State. ; and\n**(3)**\nby striking state in the heading and inserting other .\n##### (b) Effective date\nThe amendments made by this section shall apply to amounts received by an individual in taxable years beginning after December 31, 2025.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1163",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rural Veterinary Workforce Act",
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
        "updateDate": "2025-05-08T20:04:17Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2398ih.xml"
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
      "title": "Rural Veterinary Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:14:08Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Veterinary Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for an exclusion for assistance provided to participants in certain veterinary student loan repayment or forgiveness programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:37Z"
    }
  ]
}
```
