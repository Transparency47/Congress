# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7296?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7296
- Title: SAVE America Act
- Congress: 119
- Bill type: HR
- Bill number: 7296
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-04-16T08:06:49Z
- Update date including text: 2026-04-16T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7296",
    "number": "7296",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SAVE America Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:49Z",
    "updateDateIncludingText": "2026-04-16T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:32:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "AL"
    },
    {
      "bioguideId": "S001176",
      "district": "1",
      "firstName": "Steve",
      "fullName": "Rep. Scalise, Steve [R-LA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Scalise",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "UT"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "IN"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-03",
      "state": "WY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NJ"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "CO"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "TN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
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
      "sponsorshipDate": "2026-02-04",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MT"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "E000294",
      "district": "6",
      "firstName": "Tom",
      "fullName": "Rep. Emmer, Tom [R-MN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Emmer",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "MN"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "AZ"
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
      "sponsorshipDate": "2026-02-05",
      "state": "WV"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "TN"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-05",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AL"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SC"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SC"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SC"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "OH"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "MO"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AZ"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IN"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "MS"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AZ"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "MO"
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
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "OK"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "ND"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "OH"
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
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "OK"
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
      "sponsorshipDate": "2026-02-09",
      "state": "MI"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "OH"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "VA"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "UT"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
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
      "sponsorshipDate": "2026-02-09",
      "state": "ID"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "OH"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AK"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TN"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NE"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "MO"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AR"
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
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IA"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "MT"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-09",
      "state": "VA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NC"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "GA"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "WI"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "MN"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "IN"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "AL"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "KS"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "ID"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7296ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7296\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Roy introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the National Voter Registration Act of 1993 to require proof of United States citizenship to register an individual to vote in elections for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguard American Voter Eligibility Act or the SAVE America Act .\n#### 2. Ensuring only citizens are registered to vote in elections for Federal office\n##### (a) Definition of documentary proof of United States citizenship\nSection 3 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20502 ) is amended\u2014\n**(1)**\nby striking As used and inserting (a) In general .\u2014As used ; and\n**(2)**\nby adding at the end the following:\n(b) Documentary proof of United States citizenship As used in this Act, the term documentary proof of United States citizenship means, with respect to an applicant for voter registration, any of the following: (1) A form of identification issued consistent with the requirements of the REAL ID Act of 2005 that indicates the applicant is a citizen of the United States. (2) A valid United States passport. (3) The applicant's official United States military identification card, together with a United States military record of service showing that the applicant's place of birth was in the United States. (4) A valid government-issued photo identification card issued by a Federal, State or Tribal government showing that the applicant\u2019s place of birth was in the United States. (5) A valid government-issued photo identification card issued by a Federal, State or Tribal government other than an identification described in paragraphs (1) through (4), but only if presented together with one or more of the following: (A) A certified birth certificate issued by a State, a unit of local government in a State, or a Tribal government which\u2014 (i) was issued by the State, unit of local government, or Tribal government in which the applicant was born; (ii) was filed with the office responsible for keeping vital records in the State; (iii) includes the full name, date of birth, and place of birth of the applicant; (iv) lists the full names of one or both of the parents of the applicant; (v) has the signature of an individual who is authorized to sign birth certificates on behalf of the State, unit of local government, or Tribal government in which the applicant was born; (vi) includes the date that the certificate was filed with the office responsible for keeping vital records in the State; and (vii) has the seal of the State, unit of local government, or Tribal government that issued the birth certificate. (B) An extract from a United States hospital Record of Birth created at the time of the applicant's birth which indicates that the applicant\u2019s place of birth was in the United States. (C) A final adoption decree showing the applicant\u2019s name and that the applicant\u2019s place of birth was in the United States. (D) A Consular Report of Birth Abroad of a citizen of the United States or a certification of the applicant\u2019s Report of Birth of a United States citizen issued by the Secretary of State. (E) A Naturalization Certificate or Certificate of Citizenship issued by the Secretary of Homeland Security or any other document or method of proof of United States citizenship issued by the Federal government pursuant to the Immigration and Nationality Act. (F) An American Indian Card issued by the Department of Homeland Security with the classification \u2018KIC\u2019. .\n##### (b) Application of requirements\nSection 4 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20503 ) is amended by striking subsection (b) and inserting the following:\n(b) Requiring applicants To present documentary proof of United States citizenship Under any method of voter registration in a State, the State shall not accept and process an application to register to vote in an election for Federal office unless the applicant presents documentary proof of United States citizenship with the application. .\n##### (c) Registration with application for motor vehicle driver\u2019s license\nSection 5 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20504 ) is amended\u2014\n**(1)**\nin subsection (a)(1), by striking Each State motor vehicle driver's license application and inserting Subject to the requirements under section 8(j), each State motor vehicle driver's license application ;\n**(2)**\nin subsection (c)(1), by striking Each State shall include and inserting Subject to the requirements under section 8(j), each State shall include ;\n**(3)**\nin subsection (c)(2)(B)\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii), by adding and at the end; and\n**(C)**\nby adding at the end the following new clause:\n(iii) verify that the applicant is a citizen of the United States; ;\n**(4)**\nin subsection (c)(2)(C)(i), by striking (including citizenship) and inserting , including the requirement that the applicant provides documentary proof of United States citizenship ; and\n**(5)**\nin subsection (c)(2)(D)(iii), by striking ; and and inserting the following: , other than as evidence in a criminal proceeding or immigration proceeding brought against an applicant who knowingly attempts to register to vote and knowingly makes a false declaration under penalty of perjury that the applicant meets the eligibility requirements to register to vote in an election for Federal office; and .\n##### (d) Requiring documentary proof of United States citizenship with national mail voter registration form\nSection 6 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20505 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby striking Each State shall accept and use and inserting Subject to the requirements under section 8(j), each State shall accept and use ; and\n**(B)**\nby striking Federal Election Commission and inserting Election Assistance Commission ;\n**(2)**\nin subsection (b), by adding at the end the following: The chief State election official of a State shall take such steps as may be necessary to ensure that residents of the State are aware of the requirement to provide documentary proof of United States citizenship to register to vote in elections for Federal office in the State. ;\n**(3)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nin subparagraph (B) by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(C) the person did not provide documentary proof of United States citizenship when registering to vote. ; and\n**(4)**\nby adding at the end the following new subsection:\n(e) Ensuring proof of United States citizenship (1) Presenting proof of United States citizenship to election official An applicant who submits the mail voter registration application form prescribed by the Election Assistance Commission pursuant to section 9(a)(2) or a form described in paragraph (1) or (2) of subsection (a) shall not be registered to vote in an election for Federal office unless\u2014 (A) the applicant presents documentary proof of United States citizenship in person to the office of the appropriate election official not later than the deadline provided by State law for the receipt of a completed voter registration application for the election; or (B) in the case of a State which permits an individual to register to vote in an election for Federal office at a polling place on the day of the election and on any day when voting, including early voting, is permitted for the election, the applicant presents documentary proof of United States citizenship to the appropriate election official at the polling place not later than the date of the election. (2) Notification of requirement Upon receiving an otherwise completed mail voter registration application form prescribed by the Election Assistance Commission pursuant to section 9(a)(2) or a form described in paragraph (1) or (2) of subsection (a), the appropriate election official shall transmit a notice to the applicant of the requirement to present documentary proof of United States citizenship under this subsection, and shall include in the notice instructions to enable the applicant to meet the requirement. (3) Accessibility Each State shall, in consultation with the Election Assistance Commission, ensure that reasonable accommodations are made to allow an individual with a disability who submits the mail voter registration application form prescribed by the Election Assistance Commission pursuant to section 9(a)(2) or a form described in paragraph (1) or (2) of subsection (a) to present documentary proof of United States citizenship to the appropriate election official. .\n##### (e) Requirements for voter registration agencies\nSection 7 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20506 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (4)(A), by adding at the end the following new clause:\n(iv) Receipt of documentary proof of United States citizenship of each applicant to register to vote in elections for Federal office in the State. ; and\n**(B)**\nin paragraph (6)\u2014\n**(i)**\nin subparagraph (A)(i)(I), by striking (including citizenship) and inserting , including the requirement that the applicant provides documentary proof of United States citizenship ;\n**(ii)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D), respectively; and\n**(iii)**\nby inserting after subparagraph (A) the following new subparagraph:\n(B) ask the applicant the question, Are you a citizen of the United States? and if the applicant answers in the affirmative require documentary proof of United States citizenship prior to providing the form under subparagraph (C); ; and\n**(2)**\nin subsection (c)(1), by inserting who are citizens of the United States after for persons .\n##### (f) Requirements with respect to administration of voter registration\nSection 8 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20507 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking In the administration of voter registration and inserting Subject to the requirements of subsection (j), in the administration of voter registration ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (B), by striking or at the end; and\n**(ii)**\nby adding at the end the following new subparagraphs:\n(D) based on documentary proof or verified information that the registrant is not a United States citizen; or (E) the registration otherwise fails to comply with applicable State law; ;\n**(2)**\nby redesignating subsection (j) as subsection (l); and\n**(3)**\nby inserting after subsection (i) the following new subsections:\n(j) Ensuring only citizens are registered To vote (1) In general Notwithstanding any other provision of this Act, a State may not register an individual to vote in elections for Federal office held in the State unless, at the time the individual applies to register to vote, the individual provides documentary proof of United States citizenship. (2) Additional processes in certain cases (A) Process for those without documentary proof (i) In general Subject to any relevant guidance adopted by the Election Assistance Commission, each State shall establish a process under which an applicant who cannot provide documentary proof of United States citizenship under paragraph (1) may, if the applicant signs an attestation under penalty of perjury that the applicant is a citizen of the United States and eligible to vote in elections for Federal office, submit such other evidence to the appropriate State or local official demonstrating that the applicant is a citizen of the United States and such official shall make a determination as to whether the applicant has sufficiently established United States citizenship for purposes of registering to vote in elections for Federal office in the State. (ii) Affidavit requirement If a State or local official makes a determination under clause (i) that an applicant has sufficiently established United States citizenship for purposes of registering to vote in elections for Federal office in the State, such determination shall be accompanied by an affidavit developed under clause (iii) signed by the official swearing or affirming the applicant sufficiently established United States citizenship for purposes of registering to vote. (iii) Development of affidavit by the Election Assistance Commission The Election Assistance Commission shall develop a uniform affidavit for use by State and local officials under clause (ii), which shall\u2014 (I) include an explanation of the minimum standards required for a State or local official to register an applicant who cannot provide documentary proof of United States citizenship to vote in elections for Federal office in the State; and (II) require the official to explain the basis for registering such applicant to vote in such elections. (B) Process in case of certain discrepancies in documentation Subject to any relevant guidance adopted by the Election Assistance Commission, each State shall establish a process under which an applicant can provide such additional documentation to the appropriate election official of the State as may be necessary to establish that the applicant is a citizen of the United States in the event of a discrepancy with respect to the applicant\u2019s documentary proof of United States citizenship. (3) State requirements Each State shall take affirmative steps on an ongoing basis to ensure that only United States citizens are registered to vote under the provisions of this Act, which shall include the establishment of a program described in paragraph (4) not later than 30 days after the date of the enactment of this subsection. (4) Program described A State may meet the requirements of paragraph (3) by establishing a program under which the State identifies individuals who are not United States citizens using information supplied by one or more of the following sources: (A) The Department of Homeland Security through the Systematic Alien Verification for Entitlements ( SAVE ) or otherwise. (B) The Social Security Administration through the Social Security Number Verification Service, or otherwise. (C) State agencies that supply State identification cards or driver\u2019s licenses where the agency confirms the United States citizenship status of applicants. (D) Other sources, including databases, which provide confirmation of United States citizenship status. (5) Availability of information (A) In general At the request of a State election official (including a request related to a process established by a State under paragraph (2)(A) or (2)(B)), any head of a Federal department or agency possessing information relevant to determining the eligibility of an individual to vote in elections for Federal office shall, not later than 24 hours after receipt of such request, provide the official with such information as may be necessary to enable the official to verify that an applicant for voter registration in elections for Federal office held in the State or a registrant on the official list of eligible voters in elections for Federal office held in the State is a citizen of the United States, which shall include providing the official with such batched information as may be requested by the official. (B) Use of SAVE system The Secretary of Homeland Security may respond to a request received under paragraph (1) by using the system for the verification of immigration status under the applicable provisions of section 1137 of the Social Security Act ( 42 U.S.C. 1320b\u20137 ), as established pursuant to section 121(c) of the Immigration Reform and Control Act of 1986 ( Public Law 99\u2013603 ). (C) Sharing of information The heads of Federal departments and agencies shall share information with each other with respect to an individual who is the subject of a request received under paragraph (A) in order to enable them to respond to the request. (D) Investigation for purposes of removal The Secretary of Homeland Security shall conduct an investigation to determine whether to initiate removal proceedings under section 239 of the Immigration and Nationality Act ( 8 U.S.C. 1229 ) if it is determined pursuant to subparagraph (A) or (B) that an alien (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) is unlawfully registered to vote in elections for Federal office. (E) Prohibiting fees The head of a Federal department or agency may not charge a fee for responding to a State\u2019s request under paragraph (A). (k) Removal of noncitizens from registration rolls A State shall remove an individual who is not a citizen of the United States from the official list of eligible voters for elections for Federal office held in the State at any time upon receipt of documentation or verified information that a registrant is not a United States citizen. .\n##### (g) Clarification of authority of State To remove noncitizens from official list of eligible voters\n**(1) In general**\nSection 8(a)(4) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20507(a)(4) ) is amended\u2014\n**(A)**\nby striking or at the end of subparagraph (A);\n**(B)**\nby adding or at the end of subparagraph (B); and\n**(C)**\nby adding at the end the following new subparagraph:\n(C) documentary proof or verified information that the registrant is not a United States citizen; .\n**(2) Conforming amendment**\nSection 8(c)(2)(B)(i) of such Act ( 52 U.S.C. 20507(c)(2)(B)(i) ) is amended by striking (4)(A) and inserting (4)(A) or (C) .\n##### (h) Requirements with respect to Federal mail voter registration form\n**(1) Contents of mail voter registration form**\nSection 9(b) of such Act ( 52 U.S.C. 20508(b) ) is amended\u2014\n**(A)**\nin paragraph (2)(A), by striking (including citizenship) and inserting (including an explanation of what is required to present documentary proof of United States citizenship) ;\n**(B)**\nin paragraph (3), by striking and at the end;\n**(C)**\nin paragraph (4), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following new paragraph:\n(5) shall include a section, for use only by a State or local election official, to record the type of document the applicant presented as documentary proof of United States citizenship, including the date of issuance, the date of expiration (if any), the office which issued the document, and any unique identification number associated with the document. .\n**(2) Information on mail voter registration form**\nSection 9(b)(4) of such Act ( 52 U.S.C. 20508(b)(4) ) is amended\u2014\n**(A)**\nby redesignating clauses (i) through (iii) as subparagraphs (A) through (C), respectively; and\n**(B)**\nin subparagraph (C) (as so redesignated and as amended by paragraph (1)(C)), by striking ; and and inserting the following: , other than as evidence in a criminal proceeding or immigration proceeding brought against an applicant who attempts to register to vote and makes a false declaration under penalty of perjury that the applicant meets the eligibility requirements to register to vote in an election for Federal office; and .\n##### (i) Private right of action\nSection 11(b)(1) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20510(b)(1) ) is amended by striking a violation of this Act and inserting a violation of this Act, including the act of an election official who registers an applicant to vote in an election for Federal office who fails to present documentary proof of United States citizenship, .\n##### (j) Criminal penalties\nSection 12(2) of such Act ( 52 U.S.C. 20511(2) ) is amended\u2014\n**(1)**\nby striking or at the end of subparagraph (A);\n**(2)**\nby redesignating subparagraph (B) as subparagraph (D); and\n**(3)**\nby inserting after subparagraph (A) the following new subparagraphs:\n(B) in the case of an officer or employee of the executive branch, providing material assistance to a noncitizen in attempting to register to vote or vote in an election for Federal office; (C) registering an applicant to vote in an election for Federal office who fails to present documentary proof of United States citizenship; or .\n##### (k) Special rule for States not requiring voter registration\nSection 4 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20503 ), as amended by subsection (b), is amended by adding at the end the following:\n(c) Special rule for States not requiring voter registration In the case of a State or jurisdiction that does not require voter registration as a requirement to vote in an election for Federal office on or after the date of the enactment of this subsection, the State or jurisdiction shall be deemed to meet the requirements of this Act if the State or jurisdiction establishes a system for confirming the citizenship of individuals voting in an election for Federal office prior to the first day for voting with respect to such election and provides such confirmation of citizenship status for each eligible voter to election officials at the polling places during the voting period. .\n##### (l) Election Assistance Commission guidance\nNot later than 10 days after the date of the enactment of this Act, the Election Assistance Commission shall adopt and transmit to the chief State election official of each State guidance with respect to the implementation of the requirements under the National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ), as amended by this section.\n##### (m) Inapplicability of Paperwork Reduction Act\nSubchapter I of chapter 35 of title 44 (commonly referred to as the Paperwork Reduction Act ) shall not apply with respect to the development or modification of voter registration materials under the National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ), as amended by this section, including the development or modification of any voter registration application forms.\n##### (n) Duty of Secretary of Homeland Security To notify election officials of naturalization\nUpon receiving information that an individual has become a naturalized citizen of the United States, the Secretary of Homeland Security shall promptly provide notice of such information to the appropriate chief election official of the State in which such individual is domiciled.\n##### (o) Rule of construction regarding provisional ballots\nNothing in this section or in any amendment made by this section may be construed to supercede, restrict, or otherwise affect the ability of an individual to cast a provisional ballot in an election for Federal office or to have the ballot counted in the election if the individual is verified as a citizen of the United States pursuant to section 8(j) of the National Voter Registration Act of 1993 (as added by subsection (f)).\n##### (p) Rule of construction regarding effect on State exemptions from other Federal laws\nNothing in this section or in any amendment made by this section may be construed to affect the exemption of a State from any requirement of any Federal law other than the National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ).\n##### (q) Effective date\nThis section and the amendments made by this section shall take effect on the date of the enactment of this section, and shall apply with respect to applications for voter registration which are submitted on or after such date.\n#### 3. Photo voter identification required for voting in a Federal election\n##### (a) In general\nEach individual voting in an election for Federal office shall present an eligible photo identification document.\n##### (b) Presentation requirements\n**(1) In-person voting**\nIn the case of an individual who votes in-person, the eligible photo identification document shall\u2014\n**(A)**\nbe a tangible (not digital) document; and\n**(B)**\nbe presented at the time of voting.\n**(2) Absentee voting**\nIn the case of an individual voting by absentee ballot, the individual shall include a copy of the eligible photo identification document\u2014\n**(A)**\nwith the request for an absentee ballot; and\n**(B)**\nwith the submission of the absentee ballot.\n##### (c) Eligible photo identification document\nFor purposes of this section:\n**(1) In general**\nThe term eligible photo identification document means any document which\u2014\n**(A)**\nis issued by an authority described in paragraph (2); and\n**(B)**\nmeets the requirements of paragraph (3).\n**(2) Issuing authority**\nThe following are authorities described in this paragraph:\n**(A)**\nA State agency responsible for issuing State motor vehicle drivers' licenses.\n**(B)**\nA State or local election office.\n**(C)**\nA Native tribal government.\n**(D)**\nThe Department of State.\n**(E)**\nThe Department of War.\n**(F)**\nA branch of the Armed Forces.\n**(3) Requirements**\nA document meets the requirements of this paragraph if the document contains\u2014\n**(A)**\na photograph of the individual identified on the document;\n**(B)**\nan indication on the front of the document that the individual identified on the document is a United States citizen; and\n**(C)**\neither\u2014\n**(i)**\nan identification number issues by the entity described in paragraph (2)(A); or\n**(ii)**\nthe last four digits of the social security number of the individual identified on the document.\n**(4) Use of additional documentation**\n**(A) Use of additional documentation**\nA document which fails to meet the requirements of paragraph (3)(B) shall not fail to be treated as an eligible photo identification document if the document is presented together with another identification document that indicates the individual is a United States citizen.\n**(B) States using SAVE system**\n**(i) In general**\nThe requirements of paragraph (3)(B) shall not apply to an individual\u2014\n**(I)**\nwho votes in a State or jurisdiction which meets the requirements of clause (ii); and\n**(II)**\nwho registered to vote in such State or jurisdiction before the most recent date on which the State or jurisdiction last submitted its voter registration rolls to the Department of Homeland Security as provided in clause (ii)(I).\n**(ii) Requirements**\nThe requirements of this clause are met if\u2014\n**(I)**\nthe State or jurisdiction has submitted its voter registration list to the Department of Homeland Security through the Systematic Alien Verification for Entitlements (SAVE) program not less frequently than quarterly since June 1, 2025, for purposes of identifying ineligible registrations and non-citizens; and\n**(II)**\nthe State or jurisdiction indicates in each voter record on its voter rolls whether the voter has been verified as a United States citizen based on the information provided by the Department of Homeland Security under subclause (I), and the date of such verification.\n**(iii) Special rule for States not requiring voter registration**\nIn the case of a State or jurisdiction that does not require voter registration as a requirement to vote in an election for Federal office on or after the date of the enactment of this Act\u2014\n**(I)**\nclause (i)(ii) shall not apply; and\n**(II)**\nthe State or jurisdiction shall be deemed to meet the requirements of clause (ii) if the State or jurisdiction establishes a system for confirming the citizenship of individuals voting in an election for Federal office prior to the first day of the period described in section 3 with respect to such election and provides such confirmation of citizenship status for each eligible voter to election officials at the polling places during the voting period.\n##### (d) Conforming amendment\nSection 303(b) of the Help America Vote Act of 2002 ( 52 U.S.C. 21083(b) ) is amended by striking all that precedes paragraph (4).\n##### (e) Effective date\nEach State and jurisdiction shall be required to comply with the requirements of this section with respect to all elections for Federal office occurring on and after the date of the enactment of this section.",
      "versionDate": "2026-01-30",
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
        "actionDate": "2025-04-10",
        "text": "Received in the Senate."
      },
      "number": "22",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAVE Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "128",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAVE Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-29",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "3752",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAVE America Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-06",
        "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8206",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Homeland Security and Further Additional Continuing Appropriations Act, 2026",
      "type": "HR"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-09T15:30:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-30",
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
          "measure-id": "id119hr7296",
          "measure-number": "7296",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-30",
          "originChamber": "HOUSE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7296v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2026-01-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safeguard American Voter Eligibility Act or the SAVE America Act</strong></p><p>This bill requires individuals to provide documentary proof of U.S. citizenship when registering to vote, and requires photo identification to vote,\u00a0in federal elections.</p><p>Specifically, the bill prohibits states from accepting and processing an application to register to vote in a federal election unless the applicant presents documentary proof of U.S. citizenship.\u00a0The bill specifies what documents are considered acceptable proof of U.S. citizenship, such as\u00a0identification that complies with the REAL ID Act of 2005 that indicates U.S. citizenship.</p><p>Further, the bill (1) prohibits states from registering an individual to vote in a federal election unless, at the time the individual applies to register to vote, the individual provides documentary proof of U.S. citizenship; and (2) requires states to establish an alternative process to demonstrate U.S. citizenship.</p><p>Each state must take affirmative steps on an ongoing basis to ensure that only U.S. citizens are registered to vote, which shall include establishing a program to identify individuals who are not U.S. citizens using information supplied by certain sources.</p><p>Additionally, states must remove noncitizens from their official lists of eligible voters.</p><p>The bill (1) provides\u00a0for a private right of action for certain violations, and (2) establishes criminal penalties for certain offenses.</p><p>Individuals voting in federal elections must present an eligible photo identification document. An individual who votes by absentee ballot must submit a copy of their identification document with both the request for, and the submission of, the absentee ballot.</p>"
        },
        "title": "SAVE America Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7296.xml",
    "summary": {
      "actionDate": "2026-01-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safeguard American Voter Eligibility Act or the SAVE America Act</strong></p><p>This bill requires individuals to provide documentary proof of U.S. citizenship when registering to vote, and requires photo identification to vote,\u00a0in federal elections.</p><p>Specifically, the bill prohibits states from accepting and processing an application to register to vote in a federal election unless the applicant presents documentary proof of U.S. citizenship.\u00a0The bill specifies what documents are considered acceptable proof of U.S. citizenship, such as\u00a0identification that complies with the REAL ID Act of 2005 that indicates U.S. citizenship.</p><p>Further, the bill (1) prohibits states from registering an individual to vote in a federal election unless, at the time the individual applies to register to vote, the individual provides documentary proof of U.S. citizenship; and (2) requires states to establish an alternative process to demonstrate U.S. citizenship.</p><p>Each state must take affirmative steps on an ongoing basis to ensure that only U.S. citizens are registered to vote, which shall include establishing a program to identify individuals who are not U.S. citizens using information supplied by certain sources.</p><p>Additionally, states must remove noncitizens from their official lists of eligible voters.</p><p>The bill (1) provides\u00a0for a private right of action for certain violations, and (2) establishes criminal penalties for certain offenses.</p><p>Individuals voting in federal elections must present an eligible photo identification document. An individual who votes by absentee ballot must submit a copy of their identification document with both the request for, and the submission of, the absentee ballot.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119hr7296"
    },
    "title": "SAVE America Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safeguard American Voter Eligibility Act or the SAVE America Act</strong></p><p>This bill requires individuals to provide documentary proof of U.S. citizenship when registering to vote, and requires photo identification to vote,\u00a0in federal elections.</p><p>Specifically, the bill prohibits states from accepting and processing an application to register to vote in a federal election unless the applicant presents documentary proof of U.S. citizenship.\u00a0The bill specifies what documents are considered acceptable proof of U.S. citizenship, such as\u00a0identification that complies with the REAL ID Act of 2005 that indicates U.S. citizenship.</p><p>Further, the bill (1) prohibits states from registering an individual to vote in a federal election unless, at the time the individual applies to register to vote, the individual provides documentary proof of U.S. citizenship; and (2) requires states to establish an alternative process to demonstrate U.S. citizenship.</p><p>Each state must take affirmative steps on an ongoing basis to ensure that only U.S. citizens are registered to vote, which shall include establishing a program to identify individuals who are not U.S. citizens using information supplied by certain sources.</p><p>Additionally, states must remove noncitizens from their official lists of eligible voters.</p><p>The bill (1) provides\u00a0for a private right of action for certain violations, and (2) establishes criminal penalties for certain offenses.</p><p>Individuals voting in federal elections must present an eligible photo identification document. An individual who votes by absentee ballot must submit a copy of their identification document with both the request for, and the submission of, the absentee ballot.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119hr7296"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7296ih.xml"
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
      "title": "SAVE America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAVE America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguard American Voter Eligibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Voter Registration Act of 1993 to require proof of United States citizenship to register an individual to vote in elections for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T05:04:19Z"
    }
  ]
}
```
