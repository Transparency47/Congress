# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3132
- Title: CHOICE for Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3132
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-05-22T08:07:50Z
- Update date including text: 2026-05-22T08:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-06 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-06 - Committee: Ordered to be Reported by the Yeas and Nays: 12 - 11.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-06 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-06 - Committee: Ordered to be Reported by the Yeas and Nays: 12 - 11.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3132",
    "number": "3132",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "CHOICE for Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:50Z",
    "updateDateIncludingText": "2026-05-22T08:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 12 - 11.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
        "item": [
          {
            "date": "2025-05-06T14:18:54Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-01T13:02:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
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
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IL"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "WI"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "MO"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "IA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "WA"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TN"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
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
      "sponsorshipDate": "2025-06-12",
      "state": "NC"
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
      "sponsorshipDate": "2025-07-16",
      "state": "TN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AL"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "NC"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "FL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
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
      "sponsorshipDate": "2025-09-10",
      "state": "MI"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "CO"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "GA"
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
      "sponsorshipDate": "2025-10-10",
      "state": "AR"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "PA"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "WI"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "PA"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TN"
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
      "sponsorshipDate": "2025-10-28",
      "state": "OH"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NC"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
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
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MS"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "MO"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-02",
      "state": "TX"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "MN"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "NC"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "TN"
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
      "sponsorshipDate": "2025-12-17",
      "state": "FL"
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
      "sponsorshipDate": "2026-02-09",
      "state": "OK"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "AR"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "FL"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-03-30",
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
      "sponsorshipDate": "2026-04-22",
      "state": "TX"
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
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "IA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-05-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
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
      "sponsorshipDate": "2026-05-14",
      "state": "WI"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3132ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3132\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Bergman (for himself, Mr. Bost , Mr. Self , and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to allow for certain fee agreements for services rendered in the preparation, presentation, and prosecution of initial claims and supplemental claims for benefits under laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Certified Help Options in Claims Expertise for Veterans Act of 2025 or the CHOICE for Veterans Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Promotion of availability of assistance from individuals recognized by Secretary of Veterans Affairs for preparation, presentation, and prosecution of certain claims for benefits under laws administered by the Secretary.\nSec. 3. Agents and attorneys in certain claims under laws administered by Secretary of Veterans Affairs: applications for recognition; grounds for suspension; fees allowable.\nSec. 4. Penalties for certain acts during the preparation, presentation, or prosecution of claims for benefits under laws administered by the Secretary of Veterans Affairs.\nSec. 5. Comptroller General review of process for recognition of agents and attorneys for preparation, presentation, and prosecution of certain claims under laws administered by the Secretary.\nSec. 6. Publication of information with respect to recognition as agent or attorney for preparation, presentation, and prosecution of certain claims under laws administered by the Secretary; biennial review.\nSec. 7. Federal preemption.\nSec. 8. Extension of certain limits on payments of pension.\n#### 2. Promotion of availability of assistance from individuals recognized by Secretary of Veterans Affairs for preparation, presentation, and prosecution of certain claims for benefits under laws administered by the Secretary\n##### (a) Notice of availability of assistance from accredited persons\nSection 5103A of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (g) through (i) as subsections (h) through (j), respectively; or\n**(2)**\nby inserting after subsection (f) the following new subsections:\n(g) Notice of availability of representation (1) Upon receipt of a claim, or supplemental claim, by a claimant not represented by an accredited person, the Secretary shall provide notice to the claimant that\u2014 (A) an accredited person may be available to the claimant for the preparation, presentation, or prosecution of such claim or supplemental claim; (B) an organization recognized under section 5902 of this title is available to the claimant for the preparation, presentation, or prosecution of such claim or supplemental claim at no cost to the claimant; and (C) includes the web addresses of the Department websites described in paragraph (2). (2) (A) The Secretary shall maintain, on a publicly available website of the Department\u2014 (i) a list of accredited persons available to the claimant for the preparation, presentation, or prosecution of an initial claim or supplemental claim; and (ii) a system through which a claimant may report\u2014 (I) a person, who is not an accredited person, who prepared, presented, or prosecuted a claim or supplemental claim on behalf of the claimant; and (II) any fee charged by such person associated with such preparation, presentation, or prosecution. (B) With respect to the list described in paragraph (1)(A), the Secretary shall\u2014 (i) update the such list not less than quarterly; and (ii) ensure such list is easily accessible to a claimant. (3) In this subsection, the term accredited person means\u2014 (A) an organization recognized under section 5902 of this title; or (B) an attorney, agent, or other person recognized under section 5904 of this title. .\n##### (b) Online warnings of fees for certain representation\nThe Secretary of Veterans Affairs shall include, in each web portal of the Department of Veterans Affairs through which an individual may file a claim for a benefit under the laws administered by the Secretary, a warning with respect to fees an agent or attorney recognized under section 5904 of such title may charge such individual associated with the preparation, presentation, or prosecution of such claim. Such warning shall include the web addresses of the Department websites maintained pursuant to subsection (g) of section 5103A of such title, as added by subsection (a).\n##### (c) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall\u2014\n**(1)**\ncomplete a review the regulations, processes, and procedures of the Department of Veterans Affairs that with respect to the recognition of agents and attorneys under section 5904 of such title;\n**(2)**\ndevelop recommendations for legislative or administrative action to improve such regulations, processes, and procedures; and\n**(3)**\nsubmit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that includes\u2014\n**(A)**\nthe findings of the review under paragraph (1); and\n**(B)**\nthe recommendations developed under paragraph (2).\n#### 3. Agents and attorneys in certain claims under laws administered by Secretary of Veterans Affairs: applications for recognition; grounds for suspension; fees allowable\n##### (a) In general\nSection 5904 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby inserting (A) before Except ; and\n**(ii)**\nby adding at the end the following new subparagraphs:\n(B) (i) An individual desiring recognition under this section shall submit to the Secretary an application in such form, at such time, and containing such information and assurances as the Secretary has determined appropriate to recognize such individual under this section. (ii) If the Secretary cannot verify whether the individual satisfies the qualifications and standards prescribed under paragraph (2) before the end of the 180-day period beginning after the date on which the Secretary receives an application under clause (i), the Secretary shall recognize the individual on a conditional and temporary basis for a one-year period. (iii) At the end of such one-year period, the Secretary shall recognize the individual on a conditional and temporary basis for such additional 180-day periods until the date on which the Secretary can verify whether the individual satisfies such qualifications and standards. (C) (i) The Secretary may not refuse to recognize under this section an individual as an agent or attorney solely on the basis that such individual\u2014 (I) before the date of the enactment of this subparagraph\u2014 (aa) charged a claimant a fee for services rendered in the preparation, presentation, or prosecution of an initial claim; or (bb) charged a claimant a fee for such services while such individual was not recognized under this section; or (II) is an employee of a nonprofit organization and seeks recognition under this section in the official capacity of such individual. (ii) In this subparagraph, the term nonprofit organization means an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code. ; and\n**(B)**\nby adding at the end the following new paragraphs:\n(7) (A) The Secretary shall prescribe regulations to recognize an individual as an agent or attorney to render services in the preparation, presentation, and prosecution of initial claims, or a supplemental claim presented after a final decision with respect to that claim. (B) The Secretary may charge and collect an assessment from an individual who\u2014 (i) seeks recognition under this section as an agent or attorney for the preparation, presentation, and prosecution of an initial claim under the laws administered by the Secretary or a supplemental claim presented after a final decision with respect to that claim; and (ii) charges or collects fees from a claimant for services rendered in such preparation, presentation, and prosecution. (C) An assessment described in subparagraph (B) shall\u2014 (i) be in such amount as the Secretary prescribes in regulations and determines appropriate; and (ii) may not exceed $500. (D) Amounts collected under this paragraph shall be deposited in a revolving fund in the Treasury of the United States. Such amounts shall be available to the Secretary for the administration of this section. (8) (A) An individual recognized as agent or attorney under this section for the preparation, presentation, or prosecution of an initial claim, or a supplemental claim presented after a final decision with respect to that claim, may not\u2014 (i) charge any fee for services rendered in such preparation, presentation, or prosecution if\u2014 (I) the Secretary determines the disability associated with such initial claim or supplemental claim is presumed to be service-connected because the disability is a chronic disease shown as such during\u2014 (aa) a period of active military, naval, air, or space service; or (bb) the presumptive period under section 3.307 of title 38, Code of Federal Regulations (or a successor regulation); or (II) such initial claim or supplemental claim is filed while the claimant is serving on active duty; (ii) prohibit a claimant from terminating the representation agreement between the claimant and the agent or attorney prior to the date on which the agency of jurisdiction renders a decision on such initial claim or supplemental claim; (iii) charge any fee for services rendered in the preparation, presentation, and prosecution of such a supplemental claim that could have been filed in continuous pursuit of a claim within one year of the previous decision on that claim, but was filed after such previous decision became final solely due to delay on the part of the agent or attorney; or (iv) charge any fee for services rendered in the preparation, presentation, or prosecution of a supplemental claim, a request for higher-level review by the agency of original jurisdiction under section 5104B of this title, or notice of disagreement pursuant to section 5104C(a), where another individual employed by the same organization as the agent or attorney, or employed by a subsidiary of the such organization, previously charged the claimant a fee for the preparation, presentation, or prosecution of the initial claim, or the supplemental claim presented after a final decision with respect to that claim. (B) (i) Agents or attorneys recognized under this section shall, pursuant to regulations prescribed by the Secretary, file a copy of any fee agreement between the agent or attorney and a claimant for the preparation, presentation, or prosecution of an initial claim, or a supplemental claim presented after a final decision with respect to that claim. (ii) The Office of General Counsel of the Department may audit agents or attorneys recognized under this section to ensure compliance with the requirements of this paragraph. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (1) through (9) as subparagraphs (A) through (I), respectively;\n**(B)**\nby inserting (1) before The Secretary, after notice ;\n**(C)**\nin paragraph (1), as designated by subparagraph (B)\u2014\n**(i)**\nin subparagraph (H), as so redesignated, by striking subsection (c)(3)(A); or and inserting subsection (c)(2)(A) ;\n**(ii)**\nin subparagraph (I), as so redesignated, by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end the following new subparagraphs:\n(J) has failed to keep client data and personally identifiable information in accordance with applicable provisions of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1301 et seq. ), including the data security requirements and implementing regulations of that Act; (K) has sold, or otherwise received consideration for the referral of, any personally identifiable information or other data and information relating to an individual for whom the agent or attorney provided services with respect to the preparation, presentation, or prosecution of a claim under a law administered by the Secretary; (L) has entered into a fee agreement with a claimant, or otherwise received consideration from a claimant, for the preparation, presentation, or prosecution of an initial claim under the laws administered by the Secretary, or a supplemental claim presented after a final decision with respect to that claim, and referred such claimant to a private medical professional\u2014 (i) with whom the agent or attorney has a business relationship; and (ii) who would receive any fee or other consideration for the provision of any service related to such initial claim or supplemental claim; or (M) has used an overseas call center to assist with marketing, initiation, or assistance with, the preparation, presentation, or prosecution of a claim under a law administered by the Secretary. ; and\n**(D)**\nby adding at the end the following new paragraph:\n(2) Not later than one year after the date of the enactment of the Certified Help Options in Claims Expertise for Veterans Act of 2025, and annually thereafter, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report that includes with respect to the period covered by the report\u2014 (A) the number of individuals denied recognition under subsection (a); (B) for each individual denied recognition under such subsection, a statement of the reasons for such denial; (C) the number of individuals suspended or excluded from further practice pursuant to this subsection; (D) for each individual so suspended or excluded, a statement of the reasons for such suspension or exclusion; (E) the number of individuals granted temporary and conditional recognition pursuant to clause (ii) or (iii) of subsection (a)(1)(B) penalized under subsection (c) of section 5905 of this title; and (F) for each individual so penalized, a statement of the reasons for such penalty. ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby inserting Fee agreements.\u2014 after (c) ;\n**(B)**\nin paragraph (1), by striking paragraph (4) and inserting paragraph (4) or paragraph (5) ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby striking in a case referred to in paragraph (1) of this subsection ; and\n**(ii)**\nby inserting in a case after represents a person ; and\n**(D)**\nby adding at the end the following new paragraph:\n(5) (A) In connection with a proceeding before the Department with respect to benefits under laws administered by the Secretary, a fee agreement between a claimant and an agent or attorney for the preparation, presentation, or prosecution of an initial claim for such benefits or a supplemental claim presented after a final decision with respect to such claim shall be a fee agreement described in subparagraph (B). (B) (i) A fee agreement described in this subparagraph is a fee agreement\u2014 (I) that does not require payment from a claimant to the agent or attorney before the date on which the claimant is provided notice of the decision of the agency of original jurisdiction under\u2014 (aa) under section 5104 of this title with respect to the initial claim; or (bb) under section 5108 of this title with respect to the supplemental claim; (II) under which the total amount payable by the claimant to the agent or attorney\u2014 (aa) is contingent on whether the initial claim or supplemental claim presented after a final decision with respect to such claim is resolved in a manner favorable to the claimant; (bb) does not exceed the lesser of\u2014 (AA) $12,500 (as adjusted from time to time under subparagraph (E)); or (BB) the amount equal to the product of five and the amount of the monthly increase of benefits awarded to the claimant pursuant to the claim; and (III) that contains an attestation by the claimant that the agent or attorney provided to the claimant the standard form under clause (iii). (ii) For purposes of this subparagraph, an initial claim or supplemental claim presented after a final decision with respect to such claim shall be considered to have been resolved in a manner favorable to the claimant if all or any part of the relief sought pursuant to the claim is granted. (C) For use in fee agreements described in subparagraph (B), the Secretary shall develop a standard form that includes the a notice to the claimant that organizations recognized under section 5902 of this title furnish services with respect to initial claims under laws administered by the Secretary and supplemental claims for such benefits at no cost to claimants. (D) (i) If the total amount payable by a claimant to an agent or attorney under a fee agreement described in subparagraph (B) exceeds the amount of any past-due benefits awarded to the claimant pursuant to the claim associated with such fee agreement, the agent or attorney\u2014 (I) may not require the claimant to pay such total amount in a single payment; and (II) shall provide the claimant with an option to pay such total amount in incremental payments. (ii) An incremental payment under clause (i) may not exceed the amount of the monthly increase of benefits awarded to a claimant pursuant to the claim associated with such fee agreement. (E) Effective on October 1 of each year (beginning in the first fiscal year after the date of the enactment of the Certified Help Options in Claims Expertise for Veterans Act of 2025), the Secretary shall increase the dollar amount in effect under clause (i) of subparagraph (B) by a percentage equal to the percentage by which the Consumer Price Index for all urban consumers (U.S. city average) increased during the 12-month period ending with the last month for which Consumer Price Index data is available. In the event that such Consumer Price Index does not increase during such period, the Secretary shall maintain the dollar amount in effect under such clause during the previous fiscal year. .\n##### (b) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall prescribe regulations to carry out the amendments made by this section.\n#### 4. Penalties for certain acts during the preparation, presentation, or prosecution of claims for benefits under laws administered by the Secretary of Veterans Affairs\n##### (a) Penalties for unauthorized fees\n**(1) In general**\nSection 5905 of title 38, United States Code, is amended\u2014\n**(A)**\nin the section heading, by striking Penalty and inserting Penalties (and conforming the table of sections at the beginning of chapter 59 of such title accordingly);\n**(B)**\nby striking Whoever and inserting the following:\n(a) Withholding of benefits Whoever ; and\n**(C)**\nby adding at the end the following new subsections:\n(b) Charging of unauthorized fees (1) Except as provided in sections 5904 or 1984 of this title, whoever solicits, contracts for, charges, or receives, or attempts to solicit, contract for, charge, or receive, any fee or any other consideration with respect to the preparation, presentation, or prosecution of any claim for benefits under the laws administered by the Secretary shall be fined as provided in title 18, or imprisoned not more than one year, or both. (2) Paragraph (1) shall not apply to the provision of a medical examination or a medical opinion by a third party that does not have a business relationship with an individual recognized under section 5904 of this title for the preparation, presentation, or prosecution of a claim for benefits under laws administered by the Secretary. (c) Violations during conditional and temporary recognition If an individual recognized as an agent or attorney on a conditional and temporary basis pursuant to clause (ii) or (iii) of section 5904(a)(1)(B) violates any law or regulation administered by the Secretary under this chapter\u2014 (1) the Secretary shall, after notice, revoke the conditional and temporary recognition of the individual; and (2) such individual shall, after notice and opportunity for a hearing\u2014 (A) be fined $50,000; and (B) shall be barred from recognition under section 5904 of this title\u2014 (i) for a period of one year beginning on the date of the first violation; and (ii) for a period of 10 years beginning on the date of each subsequent violation. (d) Deposit of fines Any amount received by the Federal Government from a fine imposed under subsection (b) or subsection (c) shall be deposited in the fund established by section 5904(a)(7)(D) of this title. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 59 of such title is amended by striking the item relating to section 5905 and inserting the following new item:\n5905. Penalties for certain acts. .\n##### (b) Effective date\nThe amendments made by this section shall take effect on the date that is 180 days after the date on which the Secretary prescribes the regulations required by subsection (b) of section 3.\n##### (c) Regulations\nNot later than 90 days after the date of the enactment of this Act, the Secretary, acting through the General Counsel of the Department of Veterans Affairs, shall prescribe regulations to define the phrase preparation, presentation , or prosecution for purposes of subsection (b) of section 5095 of title 38, United States Code, as added by subsection (a).\n#### 5. Comptroller General review of process for recognition of agents and attorneys for preparation, presentation, and prosecution of certain claims under laws administered by the Secretary\nNot later than one year after the date of the enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\ncomplete a review of the process by which the Secretary of Veterans Affairs, under section 5904 of title 38, United States Code, as amended by this Act, recognizes agents and attorneys for the preparation, presentation, and prosecution of claims for benefits under laws administered by the Secretary; and\n**(2)**\nsubmit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that includes\u2014\n**(A)**\nan identification of deficiencies in the administration of such section, as amended by this Act; and\n**(B)**\nrecommendations of the Comptroller General with respect to legislative or administrative action to improve the administration of such section, as amended by this Act.\n#### 6. Publication of information with respect to recognition as agent or attorney for preparation, presentation, and prosecution of certain claims under laws administered by the Secretary; biennial review\n##### (a) Knowledge test\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall publish, on a publicly-available website of the Department of Veterans Affairs, and on an on-demand basis, the necessary knowledge test to satisfy the requirements for recognition under section 5904 of title 38, United States Code, as amended by this Act.\n##### (b) Continuing legal education requirements\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary shall issue regulations that\u2014\n**(A)**\nupdate the continuing legal education requirements for continued recognition as an agent or attorney under section 5904 of such title, as amended by this Act; and\n**(B)**\nincrease the amount of continuing legal education required for such recognition to an amount that is greater than the amount of such continuing legal education required for such recognition as of the date of the enactment of this Act.\n**(2) Biennial reviews**\nNot later than two years after the date on which the Secretary issues the regulations required under paragraph (1), and on a basis not less frequent than biennially thereafter, the Secretary shall conduct a review of the continuing legal education requirements for continued recognition as an agent or attorney under such section, as amended by this Act.\n#### 7. Federal preemption\nThis Act, and the amendments made by this Act, supersede any State law that is inconsistent with the rights established by this Act, or the amendments made by this Act, and preclude the implementation of such a law, whether statutory, common law, or otherwise, and whether adopted before or after the date of enactment of this Act.\n#### 8. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking November 30, 2031 and inserting April 30, 2032 .",
      "versionDate": "2025-05-01",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-05T14:23:06Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-06-05T14:23:11Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-05T14:22:45Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:54:20Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-06-05T14:23:00Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-06-05T14:22:08Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-05T14:22:31Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-05T14:22:17Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-05T14:22:37Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-06-05T14:22:23Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-06-05T14:22:52Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-06-05T14:22:01Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-05T14:21:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:19:16Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3132ih.xml"
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
      "title": "CHOICE for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHOICE for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Certified Help Options in Claims Expertise for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to allow for certain fee agreements for services rendered in the preparation, presentation, and prosecution of initial claims and supplemental claims for benefits under laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T09:03:52Z"
    }
  ]
}
```
