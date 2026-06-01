# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7230
- Title: Buying American Cotton Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7230
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-05-13T08:06:59Z
- Update date including text: 2026-05-13T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7230",
    "number": "7230",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Buying American Cotton Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:59Z",
    "updateDateIncludingText": "2026-05-13T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:04:00Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "OH"
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
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "PA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "AL"
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
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
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
      "sponsorshipDate": "2026-01-22",
      "state": "OH"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "AR"
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
      "sponsorshipDate": "2026-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
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
      "sponsorshipDate": "2026-02-02",
      "state": "MS"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-02",
      "state": "GA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "ME"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NC"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "MS"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "AL"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NM"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "GA"
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
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "OK"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "OH"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-23",
      "state": "NC"
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
      "sponsorshipDate": "2026-02-23",
      "state": "AL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
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
      "sponsorshipDate": "2026-02-24",
      "state": "VA"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "MS"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "SC"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "TN"
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
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
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
      "sponsorshipDate": "2026-03-12",
      "state": "NY"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "AR"
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
      "sponsorshipDate": "2026-03-12",
      "state": "AZ"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "AZ"
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
      "sponsorshipDate": "2026-03-17",
      "state": "SC"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "GA"
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
      "sponsorshipDate": "2026-04-06",
      "state": "WV"
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
      "sponsorshipDate": "2026-04-06",
      "state": "OH"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "NC"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "TX"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "SC"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "SC"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "AL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MS"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "OK"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "AR"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
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
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7230ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7230\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Murphy (for himself, Ms. Sewell , Mr. Rouzer , Mr. Espaillat , Mr. Kustoff , Mr. David Scott of Georgia , Mr. Carey , Mr. Davis of North Carolina , Mr. Thompson of Pennsylvania , Mr. Vicente Gonzalez of Texas , Mr. Moore of Alabama , Ms. Adams , Mr. Mann , Ms. Brown , Mr. Allen , Mr. Figures , Mr. Pfluger , Mr. Costa , Mr. Crawford , Mr. Bishop , Mr. Austin Scott of Georgia , Mr. Gray , Mr. Jackson of Texas , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a domestic cotton consumption credit.\n#### 1. Short title\nThis Act may be cited as the Buying American Cotton Act of 2026 .\n#### 2. Domestic cotton consumption credit\n##### (a) Purpose\nThe purposes of this section are\u2014\n**(1)**\nto encourage the consumption of cotton which originated in the United States, and products which are made from such cotton, and\n**(2)**\nto document the processing of such cotton through a trustworthy supply chain tracing system.\n##### (b) Allowance of credit\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Domestic cotton consumption credit (a) Credit allowed For purposes of section 38, the domestic cotton consumption credit determined under this section for any taxable year is an amount equal to the product of\u2014 (1) the documented volume of qualified cotton in an eligible article sold by the taxpayer in a qualifying sale during the taxable year, (2) the applicable percentage, and (3) the applicable cotton market price. (b) Qualifying sale; applicable percentage; applicable cotton market price (1) Qualifying sale For purposes of this section\u2014 (A) In general The term qualifying sale means, with respect to any eligible article, the first sale of such eligible article to an unrelated person. (B) Exception Such term shall not include any sale for use or consumption of an eligible article outside of the United States unless such sale results in income which is effectively connected with a trade or business in the United States. (C) Related persons Persons shall be treated as related to each other if such persons would be treated as a single employer under the regulations prescribed under section 52(b). (2) Applicable percentage For purposes of subsection (a)(2), the applicable percentage is\u2014 (A) in the case of an eligible article consisting of qualified cotton that\u2014 (i) was only subject to processing in the United States, or (ii) in addition to any processing that may have occurred within the United States, was subject to additional processing only in a country or countries with which the United States has entered into a free trade agreement or for which the United States has extended benefits through a unilateral preference program, 24 percent, and (B) in the case of an eligible article consisting of qualified cotton that was subject to additional processing at any stage of its processing in a country with which the United States has not entered into a free trade agreement or for which the United States has not extended benefits through a unilateral preference program, 18 percent. (3) Applicable cotton market price For purposes of this section, the term applicable cotton market price means, with respect to any eligible article, the average market price for qualified cotton in a recognized international market (as determined by the Secretary, in consultation with the Secretary of Agriculture) for the 3-calendar year period ending with or within the taxable year immediately preceding the taxable year in which the eligible article is sold. (c) Other definitions For purposes of this section\u2014 (1) Eligible article (A) In general The term eligible article means any product which\u2014 (i) is comprised in whole or in part of qualified cotton which is certified, under such regulations established by the Secretary in consultation with the Secretary of Agriculture, as meeting the requirements of paragraph (2)(B)(ii), (ii) is in its final condition, and (iii) is ready for retail sale to a consumer. (B) Exception Such term shall not include any product if\u2014 (i) any component of such product is an eligible article for which a credit has been allowed, or (ii) the taxpayer selling such product has been notified by the person from whom such a component was acquired that such person intended to claim such credit. (C) Final condition (i) In general For purposes of subparagraph (A)(ii), the term final condition means, with respect to any article, the physical state in which such article is presented for sale or sold for immediate resale to a consumer, determined\u2014 (I) without regard to any de minimis augmentation that could be performed on it by or on behalf of a retailer of the eligible article, and (II) without regard to packaging. (ii) De minimis augmentation For purposes of clause (i)(I), the term de minimis augmentation means any graphics or other adornment imposed on or attached to the article. (2) Qualified cotton (A) In general The term qualified cotton means extra long staple cotton (as defined in section 1111 of the Agricultural Act of 2014) or upland cotton (within the meaning of section 1207(c) of such Act) which\u2014 (i) is grown in the United States, and (ii) meets the proof of origin requirements of subparagraph (B). (B) Proof of origin requirements Cotton meets the proof of origin requirements of this subparagraph if\u2014 (i) such cotton was\u2014 (I) assigned a permanent bale identification number, or (II) meets such other requirements as the Secretary, in consultation with the Secretary of Agriculture, determines is sufficient to prove that the cotton originated in the United States, and (ii) the movement and volume of such cotton is digitally traced, under such regulations established by the Secretary in consultation with the Secretary of Agriculture, through the supply chain from its United States origin through to the last stage of processing into an eligible article. (C) Permanent bale identification number The term permanent bale identification number means the autogenerated identification number assigned by the Secretary of Agriculture to a bale of qualified cotton that was grown and ginned in the United States. (3) Free trade agreement (A) In general Except as provided by subparagraph (B), the term free trade agreement means a comprehensive bilateral or regional agreement\u2014 (i) that covers substantially all trade between the parties to the agreement, and (ii) with respect to which an implementing bill (as defined in section 151 of the Trade Act of 1974 ( 19 U.S.C. 2191 )) is enacted into law. (B) Exclusions The term free trade agreement does not include\u2014 (i) the WTO Agreement, as defined in section 2 of the Uruguay Round Agreements Act ( 19 U.S.C. 3501 ), (ii) the agreements specified in 101(d) of that Act ( 19 U.S.C. 3511(d) ), or (iii) any other multilateral agreement of the World Trade Organization or any successor entity. (4) Unilateral preference program (A) In general Except as provided by subparagraph (B), the term unilateral preference program \u2014 (i) means a program of the United States that provides preferential duty treatment to textile or apparel articles imported from a foreign country that is designated as a beneficiary of the program, and (ii) includes\u2014 (I) the African Growth and Opportunity Act ( 19 U.S.C. 3701 et seq. ) and section 506A of the Trade Act of 1974 ( 19 U.S.C. 2466a ), (II) the Caribbean Basin Economic Recovery Act ( 19 U.S.C. 2701 et seq. ), (III) section 915 of the Trade Facilitation and Trade Enforcement Act of 2015 ( 19 U.S.C. 4454 ), and (IV) any other provision of law\u2014 (aa) establishing a program that provides preferential duty treatment to textile or apparel articles imported from a foreign country that is designated as a beneficiary of the program, and (bb) that is enacted after the date of the enactment of this section. (B) Exclusion The term unilateral preference program does not include the Generalized System of Preferences under title V of the Trade Act of 1974 ( 19 U.S.C. 2461 et seq. ). (5) Processing (A) In general The term processing means any physical process, or any stage in such process, that contributes to the conversion of an item comprised in whole or in part of qualified cotton into an eligible article. (B) Exception Such term shall not include the mere physical possession, storage, movement, or packaging of cotton or any eligible article. (6) United States The term United States includes any possessions of the United States. (7) Volume The term volume means, with respect to any eligible article, the amount of qualified cotton in such article, as measured in pounds. (d) Increased credit for qualified cotton yarn and qualified cotton fabric (1) Qualified cotton yarn (A) In general At the election of the taxpayer, in the case of any eligible article which is composed in whole or in part of qualified cotton yarn\u2014 (i) this section shall be applied separately with respect to such cotton yarn, and (ii) the amount determined under subsection (a) with respect to such cotton yarn shall be equal to such amount (determined without regard to this subsection) multiplied by 1.6. (B) Qualified cotton yarn For purposes of this subsection, the term qualified cotton yarn means a strand of fiber made in the United States from qualified cotton into a form suitable for weaving, knitting, braiding, felting, webbing, or otherwise fabricating into a fabric. (2) Qualified cotton fabric (A) In general At the election of the taxpayer, in the case of any eligible article which is composed in whole or in part of qualified cotton fabric\u2014 (i) this section shall be applied separately with respect to such cotton fabric, and (ii) the amount determined under subsection (a) with respect to such cotton fabric shall be equal to such amount (determined without regard to this subsection) multiplied by 6.5. (B) Qualified cotton fabric For purposes of this subsection, the term qualified cotton fabric means any material woven, knitted, felted, or otherwise produced in the United States from, or in combination with, any fiber, yarn, or substitute thereof that was made in the United States from qualified cotton. (3) Election An election under this subsection shall be made at such time and in such form as the Secretary may be regulations provide. (e) Regulations The Secretary shall prescribe such regulations and other guidance as may be necessary or appropriate to carry out this section, including regulations or guidance\u2014 (1) to establish a system for preventing the credit allowed under this subsection more than once with respect to any amount of qualified cotton, which may include establishing a requirement to notify purchasers of eligible articles of the intent to claim the credit allowed under this section, (2) with respect to the digital tracing of cotton under subsection (c)(2)(B)(ii), which may include requirements to identify the taxpayers within the supply chain, and (3) with respect to the certification of qualified cotton under subsection (c)(1)(A)(i), which may require reporting of the specific volume of qualified cotton in the eligible article. .\n##### (c) Credit allowed as part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41), and by adding at the end the following new paragraph:\n(42) the domestic cotton consumption credit determined under section 45BB. .\n##### (d) Transfer of credit\nSection 6418(f)(1)(A) of such Code is amended by adding at the end the following:\n(xii) The domestic cotton consumption credit determined under section 45BB(a). .\n##### (e) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following item:\nSec. 45BB. Domestic cotton consumption credit. .\n##### (f) Effective date\nThe amendments made by this section shall apply to eligible articles (as defined in section 45BB of such Code, as added by subsection (b)) that are sold after the date of the enactment of this Act.",
      "versionDate": "2026-01-22",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1919",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Buying American Cotton Act of 2025",
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
        "updateDate": "2026-01-23T14:33:25Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7230ih.xml"
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
      "title": "Buying American Cotton Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Buying American Cotton Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a domestic cotton consumption credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T09:18:23Z"
    }
  ]
}
```
