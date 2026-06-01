# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1816?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1816
- Title: Improving Seniors’ Timely Access to Care Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1816
- Origin chamber: Senate
- Introduced date: 2025-05-20
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in Senate
- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-20: Introduced in Senate

## Actions

- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1816",
    "number": "1816",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Improving Seniors\u2019 Timely Access to Care Act of 2025",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-05-20T19:32:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-20T19:32:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "VA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NH"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "LA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "WV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CO"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "OK"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "OR"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "WY"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "MS"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "VA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NH"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "SD"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "AR"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "IL"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TX"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "WA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "KS"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NY"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "WA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "HI"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "RI"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NV"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "MT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "WI"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "NE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "IL"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "ND"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "FL"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "AZ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NV"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NM"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "NE"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "DE"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "MO"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "ME"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "GA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "AZ"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OK"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IN"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MI"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "ND"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CO"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "MO"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "OH"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "IA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "LA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "OH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "PA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AL"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-05-11",
      "state": "ME"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1816is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1816\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mr. Marshall (for himself, Mr. Warner , Ms. Hassan , Mr. Fetterman , Ms. Klobuchar , Mr. Cassidy , Mrs. Capito , Mr. Hickenlooper , Mr. Lankford , Mr. Merkley , Mrs. Blackburn , Ms. Lummis , Mrs. Hyde-Smith , Mr. Kaine , Mrs. Shaheen , Mr. Rounds , Mr. Padilla , Mr. Hagerty , Mr. Kim , Mr. Boozman , Mr. Durbin , Mr. Cornyn , Mrs. Murray , Mr. Moran , Mrs. Gillibrand , Ms. Cantwell , Ms. Hirono , Mr. Tillis , Mr. Booker , Ms. Smith , Mr. Welch , Mr. Whitehouse , Mr. Budd , Ms. Cortez Masto , Mr. Sheehy , Ms. Baldwin , Mr. Ricketts , Mr. Blumenthal , Ms. Warren , Ms. Duckworth , Mr. Hoeven , Mr. Scott of Florida , Mr. Kelly , Ms. Rosen , Mr. Heinrich , Mrs. Fischer , Mr. Coons , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to establish requirements with respect to the use of prior authorization under Medicare Advantage plans.\n#### 1. Short title\nThis Act may be cited as the Improving Seniors\u2019 Timely Access to Care Act of 2025 .\n#### 2. Establishing requirements with respect to the use of prior authorization under Medicare Advantage plans\n##### (a) In general\nSection 1852 of the Social Security Act ( 42 U.S.C. 1395w\u201322 ) is amended by adding at the end the following new subsection:\n(o) Prior authorization requirements (1) In general In the case of a Medicare Advantage plan that imposes any prior authorization requirement with respect to any applicable item or service (as defined in paragraph (5)) during a plan year, such plan shall\u2014 (A) beginning with plan years beginning on or after January 1, 2028\u2014 (i) establish the electronic prior authorization program described in paragraph (2); and (ii) meet the enrollee protection standards specified pursuant to paragraph (4); and (B) beginning with plan years beginning on or after January 1, 2027, meet the transparency requirements specified in paragraph (3). (2) Electronic prior authorization program (A) In general For purposes of paragraph (1)(A), the electronic prior authorization program described in this paragraph is a program that provides for the secure electronic transmission of\u2014 (i) a prior authorization request from a provider or supplier to a Medicare Advantage plan with respect to an applicable item or service to be furnished to an individual and a response, in accordance with this paragraph, from such plan to such provider or supplier; and (ii) any supporting documentation relating to such request or response. (B) Electronic transmission (i) Exclusions For purposes of this paragraph, a facsimile, a proprietary payer portal that does not meet standards specified by the Secretary, or an electronic form shall not be treated as an electronic transmission described in subparagraph (A). (ii) Standards An electronic transmission described in subparagraph (A) shall comply with applicable technical standards and other requirements to promote the standardization and streamlining of electronic transactions adopted by the Secretary. (3) Transparency requirements (A) In general For purposes of paragraph (1)(B), the transparency requirements specified in this paragraph are, with respect to a Medicare Advantage plan, the following: (i) The plan, annually and in a manner specified by the Secretary, shall submit to the Secretary the following information: (I) A list of all applicable items and services that were subject to a prior authorization requirement under the plan during the previous plan year. (II) The percentage and number of specified requests (as defined in subparagraph (F)) approved during the previous plan year by the plan in an initial determination and the percentage and number of specified requests denied during such plan year by such plan in an initial determination (both in the aggregate and categorized by each item and service). (III) The percentage and number of specified requests that were denied during the previous plan year by the plan in an initial determination and that were subsequently appealed. (IV) The number of appeals of specified requests resolved during the preceding plan year, and the percentage and number of such resolved appeals that resulted in approval of the furnishing of the item or service that was the subject of such request, categorized by each applicable item and service and categorized by each level of appeal (including judicial review). (V) The percentage and number of specified requests that were denied, and the percentage and number of specified requests that were approved, by the plan during the previous plan year through the utilization of decision support technology, artificial intelligence technology, machine-learning technology, clinical decision-making technology, or any other technology specified by the Secretary. (VI) The average and the median amount of time (in hours) that elapsed during the previous plan year between the submission of a specified request to the plan and a determination by the plan with respect to such request for each such item and service, excluding any such requests that were not submitted with the medical or other documentation required to be submitted by the plan. (VII) The percentage and number of specified requests that were excluded from the calculation described in subclause (VI) based on the plan\u2019s determination that such requests were not submitted with the medical or other documentation required to be submitted by the plan. (VIII) Information on each occurrence during the previous plan year in which, during a surgical or medical procedure involving the furnishing of an applicable item or service with respect to which such plan had approved a prior authorization request, the provider or supplier furnishing such item or service determined that a different or additional item or service was medically necessary, including a specification of whether such plan subsequently approved the furnishing of such different or additional item or service. (IX) A disclosure and description of any technology described in subclause (V) that the plan utilized during the previous plan year in making determinations with respect to specified requests. (X) The number of grievances (as described in subsection (f)) received by such plan during the previous plan year that were related to a prior authorization requirement. (XI) Such other information as the Secretary determines appropriate. (ii) The plan shall provide\u2014 (I) to each provider or supplier who seeks to enter into a contract with such plan to furnish applicable items and services under such plan, the list described in clause (i)(I) and any policies or procedures used by the plan for making determinations with respect to prior authorization requests; (II) to each such provider and supplier that enters into such a contract, access to the criteria used by the plan for making such determinations and an itemization of the medical or other documentation required to be submitted by a provider or supplier with respect to such a request; and (III) to an enrollee of the plan, upon request, access to the criteria used by the plan for making determinations with respect to prior authorization requests for an item or service. (B) Option for plan to provide certain additional information As part of the information described in subparagraph (A)(i) provided to the Secretary during a plan year, a Medicare Advantage plan may elect to include information regarding the percentage and number of specified requests made with respect to an individual and an item or service that were denied by the plan during the preceding plan year in an initial determination based on such requests failing to demonstrate that such individuals met the clinical criteria established by such plan to receive such items or services. (C) Regulations The Secretary shall, through notice and comment rulemaking, establish requirements for Medicare Advantage plans regarding the provision of\u2014 (i) access to criteria described in subparagraph (A)(ii)(II) to providers of services and suppliers in accordance with such subparagraph; and (ii) access to such criteria to enrollees in accordance with subparagraph (A)(ii)(III). (D) Publication of information The Secretary shall publish information described in subparagraph (A)(i) and subparagraph (B) on a public website of the Centers for Medicare & Medicaid Services. Such information shall be so published on an individual plan level and may in addition be aggregated in such manner as determined appropriate by the Secretary. (E) MedPac report Not later than 3 years after the date information is first submitted under subparagraph (A)(i), the Medicare Payment Advisory Commission shall submit to Congress a report on such information that includes a descriptive analysis of the use of prior authorization. As appropriate, the Commission should report on statistics including the frequency of appeals and overturned decisions. The Commission shall provide recommendations, as appropriate, on any improvement that should be made to the electronic prior authorization programs of Medicare Advantage plans. (F) Specified request defined For purposes of this paragraph, the term specified request means a prior authorization request made with respect to an applicable item or service. (4) Enrollee protection standards For purposes of paragraph (1)(A)(ii), with respect to the use of prior authorization by Medicare Advantage plans for applicable items and services, the enrollee protection standards specified in this paragraph are\u2014 (A) the adoption of transparent prior authorization programs developed in consultation with enrollees and with providers and suppliers with contracts in effect with such plans for furnishing such items and services under such plans; (B) allowing for the waiver or modification of prior authorization requirements based on the performance of such providers and suppliers in demonstrating compliance with such requirements, such as adherence to evidence-based medical guidelines and other quality criteria; and (C) conducting annual reviews of such items and services for which prior authorization requirements are imposed under such plans through a process that takes into account input from enrollees and from providers and suppliers with such contracts in effect and is based on consideration of prior authorization data from previous plan years and analyses of current coverage criteria. (5) Applicable item or service defined For purposes of this subsection, the term applicable item or service means, with respect to a Medicare Advantage plan, any item or service for which benefits are available under such plan, other than a covered part D drug. (6) Reports to Congress (A) GAO Not later than January 1, 2032, the Comptroller General of the United States shall submit to Congress a report containing an evaluation of the implementation of the requirements of this subsection and an analysis of issues in implementing such requirements faced by Medicare Advantage plans. (B) HHS (i) The Secretary Not later than the end of the fifth plan year beginning after the date of the enactment of this subsection, and biennially thereafter through the date that is 10 years after such date of enactment, the Secretary shall submit to Congress a report containing a description of the information submitted under paragraph (3)(A)(i) during\u2014 (I) in the case of the first such report, the fourth plan year beginning after the date of the enactment of this subsection; and (II) in the case of a subsequent report, the 2 plan years preceding the year of the submission of such report. (ii) CMS Not later than January 1, 2028, the Centers for Medicare & Medicaid Services and the Office of National Coordinator for Health Information Technology shall submit to Congress and publish on the internet website of the Centers for Medicare & Medicaid Services a report that\u2014 (I) defines the term real-time decision and details how the definition for such term may be updated based on any technological advances; (II) using the data submitted to the Secretary under paragraph (3)(A)(i), details a process for real-time decisions for routinely approved items and services for purposes of the electronic prior authorization program described in paragraph (2); and (III) includes an analysis of\u2014 (aa) items and services that are routinely approved; (bb) items and services identified in item (aa) that could be eligible for real-time decisions; (cc) whether establishing real-time decisions for such items and services could\u2014 (AA) improve enrollee access to benefits under this part; (BB) produce operational efficiencies for providers and suppliers and Medicare Advantage plans; and (CC) reduce health disparities for Medicare Advantage enrollees in rural and low-income communities; and (dd) how determinations of routinely approved items and services made solely through automation and artificial intelligence by Medicare Advantage plans impact patient access, including disparities in access for rural and low-income beneficiaries. .\n##### (b) Providing the Secretary authority To enforce timely responses for all prior authorization requests submitted under part C\nSection 1852(g) of the Social Security Act ( 42 U.S.C. 1395w\u201322(g) ) is amended\u2014\n**(1)**\nin paragraph (1)(A), by inserting and in accordance with any timeframe established by the Secretary under paragraph (6) after paragraph (3) ;\n**(2)**\nin paragraph (3)(B)(iii), by inserting (with respect to prior authorization requests submitted on or after the first day of the third plan year beginning after the date of the enactment of the Improving Seniors\u2019 Timely Access to Care Act of 2025, any timeframe established by the Secretary under paragraph (6)) after 72 hours ; and\n**(3)**\nby adding at the end the following new paragraph:\n(6) Timeframe for response to prior authorization requests Subject to paragraph (3), the Secretary may establish, for purposes of an organization determination made with respect to a prior authorization request for an item or service to be furnished to an individual, timeframes, such as 24 hours, for the organization to notify the enrollee (and the physician involved, as appropriate) of such determination for\u2014 (A) a request for expedited determination described in paragraph (3)(A); (B) a real time decision for routinely approved items and services; and (C) any other prior authorization request. .",
      "versionDate": "2025-05-20",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-05-20",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3514",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Seniors\u2019 Timely Access to Care Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-06-12T13:58:13Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1816is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Improving Seniors\u2019 Timely Access to Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Seniors\u2019 Timely Access to Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to establish requirements with respect to the use of prior authorization under Medicare Advantage plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:23Z"
    }
  ]
}
```
