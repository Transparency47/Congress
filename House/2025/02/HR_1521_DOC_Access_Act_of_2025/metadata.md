# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1521?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1521
- Title: DOC Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1521
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-05-13T08:06:11Z
- Update date including text: 2026-05-13T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1521",
    "number": "1521",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "DOC Access Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:11Z",
    "updateDateIncludingText": "2026-05-13T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:04:00Z",
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
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MO"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
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
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "IL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NJ"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TX"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "IN"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
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
      "sponsorshipDate": "2025-03-31",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-31",
      "state": "ID"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "KS"
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
      "sponsorshipDate": "2025-04-01",
      "state": "GA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "IL"
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
      "sponsorshipDate": "2025-04-01",
      "state": "IL"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
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
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "AR"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "KS"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "IL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "PA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NY"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "IL"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "TX"
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
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "KY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NC"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "IL"
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
      "sponsorshipDate": "2025-06-20",
      "state": "DC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-17",
      "state": "WV"
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
      "sponsorshipDate": "2025-07-17",
      "state": "AL"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "TN"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "MS"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "NY"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "TX"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "NJ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "NV"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NH"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "LA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NV"
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
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "KS"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "MS"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "SC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MI"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "UT"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "KS"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "DE"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "WA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "OH"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "MI"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
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
      "sponsorshipDate": "2025-10-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "CO"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NM"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "ME"
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
      "sponsorshipDate": "2025-11-07",
      "state": "OR"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
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
      "sponsorshipDate": "2025-11-17",
      "state": "MN"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "TX"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "SC"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "AZ"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "OR"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-17",
      "state": "PR"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "CO"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "SC"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "WA"
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
      "sponsorshipDate": "2026-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "AR"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "WV"
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
      "sponsorshipDate": "2026-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MI"
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
      "sponsorshipDate": "2026-03-12",
      "state": "VA"
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
      "sponsorshipDate": "2026-03-17",
      "state": "WA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "RI"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NM"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "TX"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "WA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "VA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "WI"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "WY"
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
      "sponsorshipDate": "2026-04-15",
      "state": "VA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "PA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-16",
      "state": "MI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "WI"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "MS"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "TN"
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
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1521ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1521\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Carter of Georgia (for himself and Ms. Clarke of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to improve health care coverage under vision and dental plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dental and Optometric Care Access Act of 2025 or the DOC Access Act of 2025 .\n#### 2. Improving health care coverage under vision and dental plans\n##### (a) In general\nTitle XXVII of the Public Health Service Act is amended by inserting after section 2719A ( 42 U.S.C. 300gg\u201319a ) the following new section:\n2719B. Improving coverage under vision and dental plans (a) In general Under a group health plan or individual or group health insurance coverage (including such a plan or coverage offering limited scope dental or vision benefits), the following shall apply: (1) Payment amounts from covered persons (A) In general The plan or coverage shall provide that, with respect to a doctor of optometry, doctor of dental surgery, doctor of dental medicine, or entity that employs such a doctor that has an agreement to participate in the plan or coverage and that provides items or services within the scope of practice of such a doctor that are not covered services under the plan or coverage to a person enrolled under such plan or coverage, such doctor or entity may charge the enrollee for such items or services any amount determined by such doctor or entity that is equal to, or less than, the usual and customary amount that such doctor or entity charges individuals who are not so enrolled for such items or services. (B) Items or services considered covered by a plan For purposes of subparagraph (A), an item or service shall be considered, with respect to a plan or coverage, to be covered services under the plan or coverage only if the item or service is an item or service with respect to which the plan or coverage is obligated to pay an amount that is reasonable and is not nominal or de minimis. (C) Exception for dental cleaning For purposes of subparagraph (A), a doctor of dental surgery, doctor of dental medicine, or entity that employs such a doctor that has an agreement to participate in the plan or coverage may charge an enrollee only the contracted network fee for any dental cleaning, including any dental cleaning that exceeds the annual maximum under the enrollee\u2019s plan or coverage. (2) Duration of limited scope vision and dental plans In the case of an agreement between such a doctor or entity and such a plan or coverage that offers limited scope dental or vision benefits\u2014 (A) the agreement may be extended for a term longer than 2 years only with the prior acceptance of such doctor or entity for each such term extension; and (B) the agreement may be extended for unlimited terms, subject to subparagraph (A). (3) No restrictions on choice of laboratories The plan or coverage may not, directly or indirectly, restrict or limit the laboratory or source or supplier of services or materials that such a doctor or entity may choose with respect to items and services within the scope of practice of such a doctor that are provided by such doctor or entity to an individual enrolled under the plan or coverage. (b) Notification The Secretary shall on an annual basis notify each State of the State\u2019s authority to enforce the provisions of subsection (a) against a group health plan or health insurance coverage described in subsection (a) pursuant to section 2723(a)(1) and request confirmation from the State whether or not the State will enforce the provisions of subsection (a). If a State notifies the Secretary that the State will not enforce the provisions of subsection (a) or fails to respond within 90 days of the Secretary\u2019s request, the Secretary shall treat such State as failing to substantially enforce such provisions for purposes of subsections (a)(2) and (b) of section 2723. (c) Relationship to exception for limited, excepted benefits Section 2722(c)(1) shall not apply with respect to the requirements of this section. (d) Election To be excluded (1) In general If a doctor of optometry, doctor of dental surgery, doctor of dental medicine, or entity that employs such a doctor to which the provisions of paragraphs (1) and (3) of subsection (a) otherwise apply makes an election under this paragraph (in such form and manner as the Secretary may by regulations prescribe), the requirements of such paragraphs insofar as they apply directly to the plan or coverage shall not apply to such plan or coverage for such period, as described in paragraph (2). (2) Period of election An election under paragraph (1)\u2014 (A) shall apply for a single specified plan year; (B) may be extended through subsequent elections under this subsection; and (C) shall not be available with respect to the requirements concerning the duration of limited scope vision and dental plans under subsection (a)(2). (e) Definitions In this section: (1) The term covered services means dental care or vision care services for which reimbursement is available under a plan or coverage contract, or for which reimbursement would be available but for the application of contractual limitations, including deductibles, copayments, coinsurance, waiting periods, lifetime maximum, frequency limitations, and alternative benefit payments. (2) The terms doctor of dental surgery and doctor of dental medicine mean a doctor of dental surgery or of dental medicine, as applicable, who is legally authorized to practice dentistry by the State in which the doctor performs such function and who is acting within the scope of the license of the doctor when performing such functions. (3) The term doctor of optometry means a doctor of optometry who is legally authorized to practice optometry by the State in which the doctor so practices. .\n##### (b) Conforming amendment\nSection 2722(c)(1) of the Public Health Service Act ( 42 U.S.C. 300gg\u201321(c)(1) ) is amended by striking The requirements and inserting Subject to section 2719B, the requirements .\n##### (c) Exclusive applicability of State law\nNotwithstanding any amendment made by this Act, State law that directly affects any standard or requirement relating to health insurance issuers and dental or vision benefit plans shall have exclusive application and the amendments made by this Act shall not apply to the extent that such State law conflicts with such amendments. The State shall retain exclusive jurisdiction over health insurance issuers and limited scope dental or vision benefit plans that are directly governed by such State.",
      "versionDate": "2025-02-24",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-07-17T18:44:34Z"
          },
          {
            "name": "Dental care",
            "updateDate": "2025-07-17T18:44:34Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-07-17T18:44:34Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-07-17T18:44:34Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-17T18:44:34Z"
          },
          {
            "name": "Hearing, speech, and vision care",
            "updateDate": "2025-07-17T18:44:34Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-17T18:44:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T15:01:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1521",
          "measure-number": "1521",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2026-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1521v00",
            "update-date": "2026-03-05"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dentist and Optometric Care Access Act of 2025 or the DOC Access Act</strong> <strong>of 20</strong><strong>25</strong></p><p>This bill prohibits private health insurance plans from setting rates for items and services, except for dental cleanings, provided by a doctor of optometry, of dental surgery, or of dental medicine\u00a0(or an employer of such a doctor) for which the plan does not pay a substantial amount.</p><p>Additionally, an agreement between a plan and such a doctor for limited scope dental or vision benefits may last longer than two years only with the prior acceptance of the doctor for each term extension. Plans also may not restrict such a doctor's choice of laboratories or suppliers.</p><p>Such doctors may elect to waive the application of the payment amount and choice of laboratories provisions of this bill.</p><p>The bill does not supersede state laws regarding health insurers and dental or vision benefit plans.</p>"
        },
        "title": "DOC Access Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1521.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dentist and Optometric Care Access Act of 2025 or the DOC Access Act</strong> <strong>of 20</strong><strong>25</strong></p><p>This bill prohibits private health insurance plans from setting rates for items and services, except for dental cleanings, provided by a doctor of optometry, of dental surgery, or of dental medicine\u00a0(or an employer of such a doctor) for which the plan does not pay a substantial amount.</p><p>Additionally, an agreement between a plan and such a doctor for limited scope dental or vision benefits may last longer than two years only with the prior acceptance of the doctor for each term extension. Plans also may not restrict such a doctor's choice of laboratories or suppliers.</p><p>Such doctors may elect to waive the application of the payment amount and choice of laboratories provisions of this bill.</p><p>The bill does not supersede state laws regarding health insurers and dental or vision benefit plans.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119hr1521"
    },
    "title": "DOC Access Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dentist and Optometric Care Access Act of 2025 or the DOC Access Act</strong> <strong>of 20</strong><strong>25</strong></p><p>This bill prohibits private health insurance plans from setting rates for items and services, except for dental cleanings, provided by a doctor of optometry, of dental surgery, or of dental medicine\u00a0(or an employer of such a doctor) for which the plan does not pay a substantial amount.</p><p>Additionally, an agreement between a plan and such a doctor for limited scope dental or vision benefits may last longer than two years only with the prior acceptance of the doctor for each term extension. Plans also may not restrict such a doctor's choice of laboratories or suppliers.</p><p>Such doctors may elect to waive the application of the payment amount and choice of laboratories provisions of this bill.</p><p>The bill does not supersede state laws regarding health insurers and dental or vision benefit plans.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119hr1521"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1521ih.xml"
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
      "title": "DOC Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DOC Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dental and Optometric Care Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to improve health care coverage under vision and dental plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:19:14Z"
    }
  ]
}
```
