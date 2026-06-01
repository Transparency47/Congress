# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5269?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5269
- Title: RESULTS Act
- Congress: 119
- Bill type: HR
- Bill number: 5269
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-05-22T08:07:44Z
- Update date including text: 2026-05-22T08:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5269",
    "number": "5269",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "RESULTS Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:44Z",
    "updateDateIncludingText": "2026-05-22T08:07:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-10T14:01:15Z",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "FL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "GA"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "AZ"
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
      "sponsorshipDate": "2025-09-10",
      "state": "NC"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "KS"
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
      "sponsorshipDate": "2025-09-10",
      "state": "NC"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "OH"
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
      "sponsorshipDate": "2025-09-10",
      "state": "AL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "UT"
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
      "sponsorshipDate": "2025-09-26",
      "state": "VA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NV"
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
      "sponsorshipDate": "2025-10-03",
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
      "sponsorshipDate": "2025-10-03",
      "state": "MN"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "FL"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "NJ"
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
      "sponsorshipDate": "2025-10-17",
      "state": "DC"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CO"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "DE"
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
      "sponsorshipDate": "2025-10-31",
      "state": "UT"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MI"
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
      "sponsorshipDate": "2025-11-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-11-10",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "TN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "OH"
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
      "sponsorshipDate": "2025-12-01",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
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
      "sponsorshipDate": "2025-12-11",
      "state": "WA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
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
      "sponsorshipDate": "2025-12-15",
      "state": "OH"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NC"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
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
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "WI"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "FL"
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
      "sponsorshipDate": "2026-01-07",
      "state": "OH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
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
      "sponsorshipDate": "2026-01-20",
      "state": "PR"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-23",
      "state": "WV"
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
      "sponsorshipDate": "2026-02-23",
      "state": "IL"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "OR"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "UT"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "WA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "IA"
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
      "sponsorshipDate": "2026-04-14",
      "state": "NC"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "IN"
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
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "CO"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sponsorshipDate": "2026-04-21",
      "state": "OH"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NV"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NC"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NC"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "TX"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5269ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5269\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Hudson (for himself, Mr. Peters , Mr. Bilirakis , Mr. Krishnamoorthi , Mr. Fitzpatrick , Mr. Carter of Georgia , Mr. Joyce of Pennsylvania , Mr. Ciscomani , Mr. Davis of North Carolina , Ms. Davids of Kansas , Ms. Ross , Mr. Balderson , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide long-term stability for Medicare beneficiary access to clinical diagnostic laboratory tests by improving the accuracy of, and feasibility of data collection for, the private payor-based fee schedule payment rates applied under the Medicare program for such tests, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reforming and Enhancing Sustainable Updates to Laboratory Testing Services Act of 2025 or the RESULTS Act .\n#### 2. Improving the accuracy and data collection feasibility of the private payor-based Medicare payment rates for clinical diagnostic laboratory tests\n##### (a) Acquiring data for widely available non-Advanced diagnostic laboratory tests from a qualifying comprehensive claims database of an independent national nonprofit entity\nSection 1834A(a) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking requirements .\u2014Subject to subparagraph (B) and inserting\nrequirements .\u2014 (i) In general Subject to subparagraph (B) and except as provided for in clause (ii) ;\n**(ii)**\nin clause (i), as added by clause (i) of this subparagraph\u2014\n**(I)**\nby striking paragraph (2) and inserting paragraph (2)(A) ;\n**(II)**\nby inserting , in accordance with the provisions of this section, before report to the Secretary ;\n**(III)**\nby striking applicable information (as defined in paragraph (3)) for a data collection period (as defined in paragraph (4)) and inserting\napplicable information (as defined in paragraph (3))\u2014 (I) for a data collection period (as defined in paragraph (4)) beginning before January 1, 2027, ;\n**(IV)**\nby striking the period at the end and inserting ; and ; and\n**(V)**\nby adding at the end the following new subclause:\n(II) for a data collection period beginning on or after January 1, 2027, for each clinical diagnostic laboratory test for which final payment is made under this part to the laboratory during such period. ; and\n**(iii)**\nby adding at the end the following new clause;\n(ii) Collection and submission of data (I) In general With respect to data collection periods for reporting periods beginning on or after January 1, 2028, and for purposes of this section, in the case of a widely available non-ADLT clinical diagnostic laboratory test (as defined in paragraph (2)(E)), the Secretary shall collect and use applicable information from a qualifying comprehensive claims database (as defined in paragraph (2)(C)) of a qualifying independent claims data entity (as defined in paragraph (2)(D)) with which the Secretary has in effect a contract under subclause (II) for each such test furnished during the respective data collection period and for which final payment is made under this part during the year in which such data collection period occurs. (II) Contract with qualifying independent claims data entity for access to applicable information As soon as practicable after the date of enactment of this clause, the Secretary shall identify and enter into a contract with a qualifying independent claims data entity for the purpose of, with respect to widely available non-ADLT clinical diagnostic laboratory tests furnished during a data collection period, such entity reporting to the Secretary applicable information from a qualifying comprehensive claims database of the entity for such tests for which final payment is made under this part during the year in which such data collection period occurs and for which there is applicable information within such database for such period. .\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking 2025 and inserting 2027 ;\n**(ii)**\nin clause (ii), by striking beginning January 1, 2026, and ending March 31, 2026 and inserting beginning January 1, 2028, and ending March 31, 2028 ; and\n**(iii)**\nin clause (iii), by striking three years and inserting 4 years ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking Definition of applicable laboratory .\u2014In this section, the term applicable laboratory means and inserting Definitions .\u2014In this section:\n(A) Applicable laboratory (i) Reporting periods before 2028 With respect to reporting periods beginning before January 1, 2028, the term applicable laboratory means ;\n**(B)**\nin subparagraph (A), as inserted by subparagraph (A) of this paragraph\u2014\n**(i)**\nin clause (i), in the second sentence, by striking paragraph and inserting clause ; and\n**(ii)**\nby adding at the end the following new clause:\n(ii) Reporting periods beginning during 2028 and subsequent years With respect to reporting periods beginning on or after January 1, 2028, the term applicable laboratory shall have the meaning given such term in section 414.502 of title 42, Code of Federal Regulations, as in effect on May 1, 2025, except without application of paragraph (3) of such section. ; and\n**(C)**\nby adding at the end the following new subparagraphs:\n(B) Non-widely available non-ADLT clinical diagnostic laboratory test The term non-widely available non-ADLT clinical diagnostic laboratory test means, with respect to a reporting period, a clinical diagnostic laboratory test that is not an advanced diagnostic laboratory test and that is not described in subparagraph (E). (C) Qualifying independent claims data entity The term qualifying independent claims data entity means an entity that satisfies each of the following criteria: (i) The entity is a national nonprofit organization that is not affiliated with any Government agency, insurance issuer, group health plan, provider of services or supplier, or other organization in the health care sector. (ii) The entity collects data and maintains a qualifying comprehensive claims database (as defined in subparagraph (D)). (iii) The entity is certified by the Secretary to be a qualified entity (as defined in paragraph (2) of section 1874(e)) with respect to having access to data described in paragraph (3) of such section. (iv) The entity, with respect to all data included in the qualifying comprehensive claims database of the entity, complies with all applicable Federal and State privacy and security requirements, including HIPAA privacy and security law (as defined in section 3009 of the Public Health Service Act). (v) The entity applies quality assurance processes to validate all data that is included in the qualifying comprehensive claims database of the entity, including comprehensive statistical testing. (D) Qualifying comprehensive claims database The term qualifying comprehensive claims database means an independent database of private payor claims data, which\u2014 (i) includes at least 50,000,000,000 claims from more than 50 private payors and claims administrators; (ii) is a statistically significant repository of claims data that is representative for all 50 States and the District of Columbia; (iii) includes only data that is validated by quality assurance processes, including comprehensive statistical testing; (iv) complies with all applicable Federal and State privacy and security requirements, as described in subparagraph (C)(iv); (v) provides for version control of claims to enable the collation and submission, for purposes of this section, of only claims representative of final payment amounts; and (vi) includes claims data with respect to widely available non-ADLT clinical diagnostic laboratory tests. (E) Widely available non-ADLT clinical diagnostic laboratory test The term widely available non-ADLT clinical diagnostic laboratory test means, with respect to a reporting period, a clinical diagnostic laboratory test that is not an advanced diagnostic laboratory test and for which, during the first 6 months of the year immediately preceding the data collection period for such reporting period, the number of providers of services and suppliers receiving payments under this section (as determined by the Secretary using the national provider identifier of the provider of services or supplier on the claim submitted for payment under this part for such test) exceeds 100. ;\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nby inserting final after The ; and\n**(B)**\nby inserting or from a qualifying comprehensive claims database pursuant to paragraph (1)(A)(ii) after reported by a laboratory under this subsection ;\n**(4)**\nin paragraph (6)\u2014\n**(A)**\nby inserting (or, with respect to a widely available non-ADLT clinical diagnostic laboratory test, the qualifying comprehensive claims database of the qualifying independent claims data entity with a contract under paragraph (1)(A)(ii)) after In the case where an applicable laboratory ;\n**(B)**\nby striking payment rate each place it appears and inserting final payment rate ;\n**(C)**\nby inserting (and such different payment rates do not relate to the same claim) after for the same payor for the same test ; and\n**(D)**\nby inserting or qualifying independent claims data entity, as applicable, after the applicable laboratory ;\n**(5)**\nin paragraph (9)(A), by inserting required to be reported by such laboratory after in reporting information ;\n**(6)**\nin paragraph (10)\u2014\n**(A)**\nby striking by a laboratory after information disclosed ; and\n**(B)**\nby inserting by a laboratory or the qualifying independent claims data entity with a contract under paragraph (1)(A)(ii) after under this subsection ; and\n**(7)**\nin paragraph (12)\u2014\n**(A)**\nby striking Regulations .\u2014Not later than June 30, 2015, and inserting\nRegulations .\u2014 (A) For data collection periods before 2027 Not later than June 30, 2015, for data collection periods beginning before January 1, 2027, ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B) For data collection periods beginning with 2027 Not later than December 31, 2026, the Secretary shall establish through notice and comment rulemaking parameters for data collection periods beginning on or after January 1, 2027. .\n##### (b) Incorporating data collection improvements into private payor-Based Medicare payment rates for clinical diagnostic laboratory tests that are not advanced diagnostic laboratory tests\n**(1) Calculation of weighted median of private payor-based rates**\nSection 1834A(b)(2) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b)(2) ) is amended\u2014\n**(A)**\nby inserting and, in the case of widely available non-ADLT clinical diagnostic laboratory tests, with respect to data collection periods for reporting periods beginning on or after January 1, 2028, for each such test furnished by an applicable laboratory with respect to which there is applicable information made available to the Secretary pursuant to paragraph (1)(A)(ii)) of such subsection after under subsection (a) for a data collection period ; and\n**(B)**\nby inserting final before payment rates reported .\n**(2) Default adjustment in cases of widely available non-ADLT clinical diagnostic laboratory tests for periods for which there is no contract with a qualifying independent claims entity or no applicable information in the qualifying comprehensive claims database**\nSection 1834A(b) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by striking paragraph (3) and inserting paragraphs (3) and (6) ; and\n**(B)**\nby adding at the end the following new paragraph:\n(6) Default payment for widely available non-ADLT clinical diagnostic laboratory tests for periods for which there is no contract with an independent entity or with respect to which there is no data (A) In general With respect to data collection periods for reporting periods beginning on or after January 1, 2028, in the case of a widely available non-ADLT clinical diagnostic laboratory test with respect to which subsection (c) does not apply, if a circumstance described in subparagraph (B) applies with respect to such a reporting period and such a clinical diagnostic laboratory test, payment for such test under this section for a year beginning during the qualified rate period described in subparagraph (C), shall be equal to the amount of payment for such clinical diagnostic laboratory test under this section for the previous year, increased by the percentage increase in the Consumer Price Index for all urban consumers (all items; United States city average) over the previous year. (B) Circumstances described For purposes of subparagraph (A), with respect to a data collection period and a widely available non-ADLT clinical diagnostic laboratory test, the circumstances described in this subparagraph are if the Secretary\u2014 (i) is not able to enter into a contract under subsection (a)(1)(A)(ii) with a qualifying independent claims data entity with respect to such data collection period; or (ii) determines that there is no applicable information with respect to such clinical diagnostic laboratory test and data collection period in the qualifying comprehensive claims database of such qualifying independent claims data entity. (C) Qualified rate period described For purposes of subparagraph (A), the qualified rate period, with respect to a data collection period and a widely available non-ADLT clinical diagnostic test to which a circumstance described in subparagraph (B) applies, is the period\u2014 (i) beginning on the first day of the second year following the first data collection period with respect to which such circumstance applies with respect to such test; and (ii) ending with the last day of the year following the first data collection period with respect to which such circumstance no longer applies with respect to such test. .\n**(3) Payment in cases in which there is no reported applicable information for non-widely available non-ADLTs**\nSection 1834A of the Social Security Act ( 42 U.S.C. 1395m\u20131 ), is amended\u2014\n**(A)**\nin subsection (b), as amended by paragraph (2)\u2014\n**(i)**\nin paragraph (1)(A), by striking paragraphs (3) and (6) and inserting paragraphs (3), (6), and (7) ; and\n**(ii)**\nby adding at the end the following new paragraph:\n(7) Payment for non-widely available non-ADLT clinical diagnostic laboratory tests for which there is no applicable information (A) In general For determining payment under this subsection for a year in the case of a non-widely available non-ADLT clinical diagnostic laboratory test with respect to which subsection (c) does not apply, if the Secretary determines that no applicable information has been reported under subsection (a)(1)(A)(i) by any applicable laboratory for such test with respect to the most recent data collection period (beginning with data collection periods for reporting periods beginning on or after January 1, 2028), payment for such test under this section for such year shall be determined as follows: (i) In the case that a process described in subparagraph (B) was not applied pursuant to this subparagraph for determining payment for such test for a previous year with respect to such data collection period, payment for such test and year shall be determined using such a process. (ii) In the case that a process described in subparagraph (B) was applied pursuant to this subparagraph for determining payment for such test for a previous year with respect to such data collection period, payment for such test and year shall be equal to the amount of payment for such test under this section for the previous year. (B) Process described For purposes of subparagraph (A), a process described in this subparagraph, with respect to a non-widely available non-ADLT clinical diagnostic laboratory test for which there is no reported data (as described in such subparagraph) with respect to a data collection period, is\u2014 (i) cross-walking (as described in section 414.508(a) of title 42, Code of Federal Regulations, or any successor regulation) to the most appropriate clinical diagnostic laboratory test under the fee schedule under this section during that period; or (ii) if no other clinical diagnostic laboratory test is comparable to the test for which there is no reported applicable information, according to the gapfilling process described in subsection (c)(2). ; and\n**(B)**\nin subsection (c)(3), by inserting or subsection (b)(7) after under this subsection .\n**(4) Publicly available explanation of payment rates**\nSection 1834A(b) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b) ), as amended by paragraphs (2) and (3)(A), is amended by adding at the end the following new paragraph:\n(8) Explanation of payment rates In the case of a clinical diagnostic laboratory test for which payment is made under this subsection, the Secretary shall make available to the public an explanation of the payment rate for such test, including any supporting data as may be necessary for a laboratory to assess the accuracy of the calculations. .\n**(5) Technical correction clarifying period of application of market rates**\nSection 1834A(b)(4)(A) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b)(4)(A) ) is amended by striking until the year following and inserting through the year following .\n##### (c) Additional improvements To ensure updated, accurate market-Based data for clinical diagnostic laboratory tests\n**(1) Updates to applicable information to better reflect final payment rates**\nSection 1834A(a)(3) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a)(3) ) is amended\u2014\n**(A)**\nin the heading, by inserting and final payment rate after information ;\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nin the heading, by striking In general and inserting Data collection periods before January 1, 2027 ; and\n**(ii)**\nin the matter preceding clause (i)\u2014\n**(I)**\nby striking subparagraph (B) and inserting subparagraph (C) ; and\n**(II)**\nby inserting beginning before January 1, 2027 after for a data collection period ;\n**(C)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(D)**\nby inserting after subparagraph (A) the following new subparagraph:\n(B) Subsequent data collection periods In this section, subject to subparagraph (C), for a data collection period beginning on or after January 1, 2027, the term applicable information means\u2014 (i) with respect to a widely available non-ADLT clinical diagnostic laboratory test furnished during such period\u2014 (I) the final payment rate (as determined in accordance with paragraph (5) and defined in subparagraph (D)) that was paid by each private payor for the test during the year in which such period occurs; and (II) the volume, for each such payor, of such test for which final payment was made during such year; and (ii) with respect to a non-widely available non-ADLT clinical diagnostic laboratory test or an advanced diagnostic laboratory test\u2014 (I) the final payment rate (as determined in accordance with paragraph (5) and defined in subparagraph (D)) that was paid by each private payor for the test during the data collection period; and (II) the volume, for each such payor, of such test for which final payment was made during such period. ; and\n**(E)**\nby inserting after subparagraph (C), the following new subparagraph:\n(D) Final payment rate In this section, for a data collection period beginning on or after January 1, 2027, the term final payment rate \u2014 (i) means\u2014 (I) with respect to a widely available non-ADLT clinical diagnostic laboratory test furnished during a data collection period, the last payment made for a test during the year in which the data collection period occurs; and (II) with respect to a non-widely available non-ADLT clinical diagnostic laboratory test or an advanced diagnostic laboratory test paid during a data collection period, the last payment made during the data collection period; and (ii) does not include\u2014 (I) denied payments; (II) payments under appeal or under review by the private payor; (III) payments made in error; or (IV) payments that are recouped by the private payor. .\n**(2) Updating data collection periods**\nSection 1834A(a)(4)(B) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a)(4)(B) ) is amended\u2014\n**(A)**\nby striking January 1, 2019 and inserting January 1, 2027 ;\n**(B)**\nby striking June 30, 2019 and inserting June 30, 2027 ; and\n**(C)**\nby adding at the end the following new sentence: In the case of the reporting period after the reporting period described in paragraph (1)(B)(ii) and each subsequent reporting period with respect to clinical diagnostic laboratory tests that are not advanced diagnostic laboratory tests, the term data collection period means the 6-month period beginning January 1st of the year preceding the year during which such reporting period begins. .\n**(3) Ensuring data is market-based by excluding rates of Medicaid managed care organizations**\nSection 1834A(a)(8)(C) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a)(8)(C) ) is amended by striking A medicaid managed care organization and inserting With respect to data collection periods for reporting periods beginning before January 1, 2028, a medicaid managed care organization. .\n**(4) Modifications to limits on payment reductions**\nSection 1834A(b)(3) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b)(3) ) is amended\u2014\n**(A)**\nin subparagraph (A), by striking each of 2017 through 2028 and inserting 2017 and each subsequent year ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (ii), by striking 2025 and inserting 2028 ; and\n**(ii)**\nin clause (iii), by striking for each of 2026 through 2028, 15 percent and inserting for 2029 and each subsequent year, 5 percent ; and\n**(C)**\nin subparagraph (C)(ii), by inserting laboratory after advanced diagnostic .\n**(5) Sunsetting review limitations**\nSection 1834A(h)(1) of the Social Security Act ( 42 U.S.C. 1395m\u20131(h)(1) ) is amended by inserting before January 1, 2029 before the period at the end.",
      "versionDate": "2025-09-10",
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
        "actionDate": "2025-09-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2761",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RESULTS Act",
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
        "updateDate": "2025-09-23T16:55:33Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5269ih.xml"
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
      "title": "RESULTS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESULTS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reforming and Enhancing Sustainable Updates to Laboratory Testing Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide long-term stability for Medicare beneficiary access to clinical diagnostic laboratory tests by improving the accuracy of, and feasibility of data collection for, the private payor-based fee schedule payment rates applied under the Medicare program for such tests, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:48:33Z"
    }
  ]
}
```
