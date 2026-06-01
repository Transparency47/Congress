# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1261?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1261
- Title: CONNECT for Health Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1261
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2026-05-04T15:19:34Z
- Update date including text: 2026-05-04T15:19:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1261",
    "number": "1261",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "CONNECT for Health Act of 2025",
    "type": "S",
    "updateDate": "2026-05-04T15:19:34Z",
    "updateDateIncludingText": "2026-05-04T15:19:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
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
            "date": "2025-04-02T20:29:13Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-02T20:29:13Z",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MS"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "VA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "VT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "WY"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "SD"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "OK"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "WA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CO"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AK"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "WV"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "OR"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "WY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "VA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "ND"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NH"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "AZ"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "KS"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NM"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "LA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NC"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-02",
      "state": "ME"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "WV"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "DE"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MO"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "RI"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AK"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NV"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "ND"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NJ"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "IA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "IL"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "SD"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-02",
      "state": "VT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "KS"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "AZ"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "IN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NM"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "ME"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NE"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "OK"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MA"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "SC"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MD"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "GA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AR"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CO"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "LA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MI"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "OH"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MA"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "IN"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NV"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "MT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "WA"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "KY"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "MD"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1261is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1261\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Schatz (for himself, Mr. Wicker , Mr. Warner , Mrs. Hyde-Smith , Mr. Welch , Mr. Barrasso , Mr. Padilla , Mr. Thune , Ms. Smith , Mr. Lankford , Ms. Cantwell , Mr. Tuberville , Mr. Hickenlooper , Mr. Cotton , Ms. Klobuchar , Mr. Sullivan , Mr. Fetterman , Mrs. Capito , Mr. Merkley , Ms. Lummis , Mr. Kaine , Mr. Cramer , Mrs. Shaheen , Mrs. Britt , Mr. Gallego , Mr. Moran , Mr. Luj\u00e1n , Mr. Cassidy , Mr. Blumenthal , Mr. Tillis , Mr. King , Mr. Justice , Mr. Coons , Mr. Schmitt , Mr. Whitehouse , Ms. Murkowski , Ms. Rosen , Mr. Hoeven , Mr. Booker , Mr. Grassley , Ms. Duckworth , Mr. Rounds , Mr. Sanders , Mr. Marshall , Mr. Kelly , Mrs. Fischer , Mrs. Gillibrand , Mr. Young , Mr. Heinrich , Ms. Collins , Mr. Peters , Mr. Ricketts , Mr. Schiff , Mr. Mullin , Ms. Warren , Mr. Graham , Mr. Van Hollen , Mr. Daines , Mr. Warnock , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to expand access to telehealth services, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Creating Opportunities Now for Necessary and Effective Care Technologies (CONNECT) for Health Act of 2025 or the CONNECT for Health Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings and sense of Congress.\nTITLE I\u2014Removing barriers to telehealth coverage\nSec. 101. Removing geographic requirements for telehealth services.\nSec. 102. Expanding originating sites.\nSec. 103. Expanding authority for practitioners eligible to furnish telehealth services.\nSec. 104. Federally qualified health centers and rural health clinics.\nSec. 105. Native American health facilities.\nSec. 106. Repeal of six-month in-person visit requirement for telemental health services.\nSec. 107. Waiver of telehealth requirements during public health emergencies.\nSec. 108. Use of telehealth in recertification for hospice care.\nTITLE II\u2014Program integrity\nSec. 201. Clarification for fraud and abuse laws regarding technologies provided to beneficiaries.\nSec. 202. Additional resources for telehealth oversight.\nSec. 203. Addressing significant outlier billing patterns for telehealth services.\nTITLE III\u2014Beneficiary and provider supports, quality of care, and data\nSec. 301. Beneficiary engagement on telehealth.\nSec. 302. Provider supports on telehealth.\nSec. 303. Ensuring the inclusion of telehealth in measuring quality of care.\nSec. 304. Posting of information on telehealth services.\n#### 2. Findings and sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe use of technology in health care and coverage of telehealth services are rapidly evolving.\n**(2)**\nResearch has found that telehealth services can expand access to care, improve the quality of care, and reduce spending.\n**(3)**\nIn 2023, 90 percent of patients receiving telehealth services were satisfied with their experiences.\n**(4)**\nHealth care workforce shortages are a significant problem in many areas and for many types of health care clinicians.\n**(5)**\nTelehealth increases access to care in areas with workforce shortages and for individuals who live far away from health care facilities, have limited mobility or transportation, or have other barriers to accessing care.\n**(6)**\nThe use of health technologies can strengthen the expertise of the health care workforce, including by connecting clinicians to specialty consultations.\n**(7)**\nPrior to the COVID\u201319 pandemic, the utilization of telehealth services in the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) was low, accounting for 0.1 percent of Medicare Part B visits in 2019.\n**(8)**\nTelehealth now represents a critical component of care delivery. In 2023, 24 percent of Medicare fee-for-service beneficiaries received a telehealth service.\n**(9)**\nLong-term certainty about coverage of telehealth services under the Medicare program is necessary to fully realize the benefits of telehealth.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nhealth care providers can furnish safe, effective, and high-quality health care services through telehealth;\n**(2)**\nthe Secretary of Health and Human Services should promptly take all necessary measures to ensure that providers and beneficiaries can continue to furnish and utilize, respectively, telehealth services in the Medicare program, and support recent modifications to the definition of interactive telecommunications system in regulations and program instruction under the Medicare program to ensure that providers can utilize all appropriate means and types of technology, including audio-visual, audio-only, and other types of technologies, to furnish telehealth services; and\n**(3)**\nbarriers to the use of telehealth should be removed.\nI\nRemoving barriers to telehealth coverage\n#### 101. Removing geographic requirements for telehealth services\nSection 1834(m)(4)(C) of the Social Security Act ( 42 U.S.C. 1395m(m)(4)(C) ) is amended\u2014\n**(1)**\nin clause (i), in the matter preceding subclause (I), by striking clause (iii) and inserting clauses (iii) and (iv) ; and\n**(2)**\nby adding at the end the following new clause:\n(iv) Removal of geographic requirements The geographic requirements described in clause (i) shall not apply with respect to telehealth services furnished on or after October 1, 2025. .\n#### 102. Expanding originating sites\n##### (a) In general\nSection 1834(m)(4)(C)(iii) of the Social Security Act ( 42 U.S.C. 1395m(m)(4)(C)(iii) ) is amended by striking In the case that and all that follows through September 30, 2025, and inserting Beginning on the date of the enactment of the CONNECT for Health Act of 2025 , .\n##### (b) Conforming amendments\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) is amended\u2014\n**(1)**\nin paragraph (2)(B)(iii), by striking In the case that and all that follows through September 30, 2025, and inserting With respect to telehealth services furnished on or after the date of the enactment of the CONNECT for Health Act of 2025 , ; and\n**(2)**\nin paragraph (4)(C)(ii)(X), by striking , but only for purposes of section 1881(b)(3)(B) or telehealth services described in paragraph (7) .\n#### 103. Expanding authority for practitioners eligible to furnish telehealth services\nSection 1834(m)(4)(E) of the Social Security Act ( 42 U.S.C. 1395m(m)(4)(E) ) is amended\u2014\n**(1)**\nby striking Practitioner .\u2014The term and inserting \u201c Practitioner .\u2014\n(i) In general Subject to clause (ii), the term ; and\n**(2)**\nby adding at the end the following new clause:\n(ii) Expanding practitioners eligible to furnish telehealth services (I) In general Notwithstanding any other provision of this subsection, in the case of telehealth services furnished on or after October 1, 2025, the Secretary may waive any limitation on the types of practitioners who are eligible to furnish telehealth services if the Secretary determines that such waiver is clinically appropriate. (II) Implementation In implementing a waiver under this clause, the Secretary may establish requirements, as appropriate, for practitioners under such waiver, including with respect to beneficiary and program integrity protections. (III) Public comment The Secretary shall establish a process by which stakeholders may (on at least an annual basis) provide public comment on such waiver under this clause. (IV) Periodic review The Secretary shall periodically, but not more frequently than every 3 years, reassess the waiver under this clause to determine whether such waiver continues to be clinically appropriate. The Secretary shall terminate any waiver that the Secretary determines is no longer clinically appropriate. .\n#### 104. Federally qualified health centers and rural health clinics\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) is amended\u2014\n**(1)**\nin paragraph (4)(C)(i), in the matter preceding subclause (I), by striking and (7) and inserting (7), and (8) ; and\n**(2)**\nin paragraph (8)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the matter preceding clause (i), by striking During and all that follows through September 30, 2025 and inserting the following: Beginning on the first day of the emergency period described in section 1135(g)(1)(B) ;\n**(ii)**\nin clause (ii), by striking and at the end;\n**(iii)**\nby redesignating clause (iii) as clause (iv); and\n**(iv)**\nby inserting after clause (ii) the following new clause:\n(iii) the geographic requirements described in paragraph (4)(C)(i) shall not apply with respect to such a telehealth service; and ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the subparagraph heading, by inserting during initial period after rule ;\n**(ii)**\nin the first sentence of clause (i) by striking during the periods for which subparagraph (A) applies and inserting during the period beginning on the first day of the emergency period and ending on September 30, 2025 ; and\n**(iii)**\nin clause (ii), by striking Costs associated and inserting During the period for which clause (i) applies, costs associated ;\n**(C)**\nby adding at the end the following new subparagraph:\n(C) Payment after initial period (i) In general A telehealth service furnished by a Federally qualified health center or a rural health clinic to an individual pursuant to this paragraph on or after October 1, 2025, shall be deemed to be so furnished to such individual as an outpatient of such clinic or facility (as applicable) for purposes of paragraph (1) or (3), respectively, of section 1861(aa) and payable as a Federally qualified health center service or rural health clinic service (as applicable) under the prospective payment system established under section 1834(o) or under section 1833(a)(3), respectively. (ii) Treatment of costs for FQHC PPS calculations and RHC AIR calculations Costs associated with the furnishing of telehealth services by a Federally qualified health center or rural health clinic serving as a distant site pursuant to this paragraph on or after October 1, 2025, shall be considered allowable costs for purposes of the prospective payment system established under section 1834(o) and any payment methodologies developed under section 1833(a)(3), as applicable. .\n#### 105. Native American health facilities\n##### (a) In general\nSection 1834(m)(4)(C) of the Social Security Act ( 42 U.S.C. 1395m(m)(4)(C) ), as amended by section 101, is amended\u2014\n**(1)**\nin clause (i), by striking and (iv) and inserting , (iv), and (v) ; and\n**(2)**\nby adding at the end the following new clause:\n(v) Native American health facilities With respect to telehealth services furnished on or after January 1, 2026, the originating site requirements described in clauses (i) and (ii) shall not apply with respect to a facility of the Indian Health Service, whether operated by such Service, or by an Indian tribe (as that term is defined in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 )) or a tribal organization (as that term is defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )), or a facility of the Native Hawaiian health care systems authorized under the Native Hawaiian Health Care Improvement Act ( 42 U.S.C. 11701 et seq. ). .\n##### (b) No originating site facility fee for Certain Native American facilities\nSection 1834(m)(2)(B)(i) of the Social Security Act ( 42 U.S.C. 1395m(m)(2)(B)(i) ) is amended, in the matter preceding subclause (I), by inserting (other than an originating site that is only described in clause (v) of paragraph (4)(C), and does not meet the requirement for an originating site under clauses (i) and (ii) of such paragraph) after the originating site .\n#### 106. Repeal of six-month in-person visit requirement for telemental health services\n##### (a) In general\nSection 1834(m)(7) of the Social Security Act ( 42 U.S.C. 1395m(m)(7)(B) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking , subject to subparagraph (B), ;\n**(2)**\nby striking (A) In general .\u2014The geographic and inserting The geographic ; and\n**(3)**\nby striking subparagraph (B).\n##### (b) Rural health clinics\nSection 1834(y)(2) of the Social Security Act ( 42 U.S.C. 1395m(y)(2) ) is amended by striking prior to October 1, 2025 .\n##### (c) Federally qualified health centers\nSection 1834(o)(4)(B) of the Social Security Act ( 42 U.S.C. 1395m(o)(4)(B) ) is amended by striking prior to October 1, 2025 .\n#### 107. Waiver of telehealth requirements during public health emergencies\nSection 1135(g)(1) of the Social Security Act ( 42 U.S.C. 1320b\u20135(g)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), in the matter preceding clause (i), by striking subparagraph (B) and inserting subparagraphs (B) and (C) ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(C) Exception for waiver of telehealth requirements during public health emergencies For purposes of subsection (b)(8), in addition to the emergency period described in subparagraph (B), an emergency area is a geographical area in which, and an emergency period is the period during which, there exists a public health emergency declared by the Secretary pursuant to section 319 of the Public Health Service Act on or after the date of enactment of this subparagraph. .\n#### 108. Use of telehealth in recertification for hospice care\n##### (a) In general\nSection 1814(a)(7)(D)(i)(II) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(D)(i)(II) ) is amended by striking during the emergency period and all that follows through September 30, 2025 and inserting the following: during and after the emergency period described in section 1135(g)(1)(B) .\n##### (b) GAO report\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report evaluating the impact of section 1814(a)(7)(D)(i)(II) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(D)(i)(II) ), as amended by subsection (a), on\u2014\n**(1)**\nthe number and percentage of beneficiaries recertified for the Medicare hospice benefit at 180 days and for subsequent benefit periods, to the extent such data is available;\n**(2)**\nFederal oversight of the appropriateness for hospice care of the patients recertified through the use of telehealth; and\n**(3)**\nany other factors determined appropriate by the Comptroller General.\nII\nProgram integrity\n#### 201. Clarification for fraud and abuse laws regarding technologies provided to beneficiaries\nSection 1128A(i)(6) of the Social Security Act (42 U.S.C. 1320a\u20137a(i)(6)) is amended\u2014\n**(1)**\nin subparagraph (I), by striking ; or and inserting a semicolon;\n**(2)**\nin subparagraph (J), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(K) the provision of technologies (as defined by the Secretary) on or after the date of the enactment of this subparagraph, by a provider of services or supplier (as such terms are defined for purposes of title XVIII) directly to an individual who is entitled to benefits under part A of title XVIII, enrolled under part B of such title, or both, for the purpose of furnishing telehealth services, remote patient monitoring services, or other services furnished through the use of technology (as defined by the Secretary), if\u2014 (i) the technologies are not offered as part of any advertisement or solicitation; and (ii) the provision of the technologies meets any other requirements set forth in regulations promulgated by the Secretary. .\n#### 202. Additional resources for telehealth oversight\nIn addition to amounts otherwise available, there are authorized to be appropriated to the Inspector General of the Department of Health and Human Services for each of fiscal years 2026 through 2030, out of any money in the Treasury not otherwise appropriated, $3,000,000, to remain available until expended, for purposes of conducting audits, investigations, and other oversight and enforcement activities with respect to telehealth services, remote patient monitoring services, or other services furnished through the use of technology (as defined by the Secretary).\n#### 203. Addressing significant outlier billing patterns for telehealth services\n##### (a) Identification and notification of outlier billers of telehealth\n**(1) In general**\nThe Secretary shall, using standard unique health identifiers (described in section 1173(b) of the Social Security Act ( 42 U.S.C. 1320d\u20132 ) reported on claims for telehealth services furnished to individuals under section 1834(m) of such Act ( 42 U.S.C. 1395m(m) ), identify physicians and practitioners that demonstrate significant outlier billing patterns (such as coding of telehealth services for inappropriate length of time and inaccurate complexity and inappropriate or duplicate billing) for telehealth services or items or services ordered or prescribed concurrent to a telehealth service over a period of time specified by the Secretary.\n**(2) Establishment of thresholds**\nFor purposes of this subsection, the Secretary shall establish thresholds for outlier billing patterns to identify whether a physician or practitioner is a significant outlier biller for telehealth services or items or services ordered or prescribed concurrent to a telehealth service as compared to other physicians or practitioners within the same specialty and geographic area.\n##### (b) Notification\n**(1) In general**\nThe Secretary shall notify physicians and practitioners identified as a significant outlier biller for telehealth services or items or services ordered or prescribed concurrent to a telehealth service under subsection (a). Each notification under the preceding sentence shall include the following:\n**(A)**\nInformation on how the physician or practitioner compares to physicians or practitioners within the same specialty and geographic area with respect to billing for telehealth services or items or services ordered or prescribed concurrent to a telehealth service under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n**(B)**\nInformation on telehealth billing guidelines under the Medicare program.\n**(C)**\nOther information determined appropriate by the Secretary.\n**(2) Clarification**\nNothing in this subsection or subsection (a) shall be construed as directing the Centers for Medicare & Medicaid Services to pursue further audits of providers of services and suppliers outside of those permitted or required under titles XI or XVIII of the Social Security Act, or otherwise under applicable Federal law.\n##### (c) Public Availability of Information\nThe Secretary shall make aggregate information on outlier billing patterns identified under subsection (a) available on the internet website of the Centers for Medicare & Medicaid Services. Such information shall be in a form and manner determined appropriate by the Secretary and shall not identify any specific physician or practitioner.\n##### (d) Other activities\nNothing in this section shall preclude the Secretary from conducting activities that provide physicians and practitioners with information as to how they compare to other physicians and practitioners that are in addition to the activities under this section.\n##### (e) Telehealth resource centers education activities\nSection 330I(j)(2) of the Public Health Service Act ( 42 U.S.C. 254c\u201314(j)(2) ) is amended\u2014\n**(1)**\nin subparagraph (F), by striking and at the end;\n**(2)**\nin subparagraph (G), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(H) providing technical assistance and education to physicians and practitioners that the Secretary identifies pursuant to section 203(a) of the CONNECT for Health Act of 2025 as having significant levels of outlier billing patterns with respect to telehealth services or items or services ordered or prescribed concurrent to a telehealth service under the Medicare program under title XVIII of the Social Security Act, including\u2014 (i) education on practices to ensure coding of telehealth services for appropriate length of time and accurate complexity; (ii) education on prevention of inappropriate or duplicate billing; (iii) information provided in the annual physician fee schedule rulemaking regarding\u2014 (I) services specified in paragraph (4)(F)(i) of section 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) for authorized payment under paragraph (1) of such section; and (II) the process used to update such services under paragraph (4)(F)(ii) of such section 1834(m); and (iv) referral to the appropriate medicare administrative contractor for specific questions that fall outside of the scope of broad best practices. .\n##### (f) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(2) Telehealth service**\nThe term telehealth service has the meaning given that term in section 1834(m)(4)(F) of the Social Security Act ( 42 U.S.C. 1395m(m)(4)(F) ).\n**(3) Physician; practitioner**\nThe terms physician and practitioner have the meaning given those terms for purposes of section 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ).\nIII\nBeneficiary and provider supports, quality of care, and data\n#### 301. Beneficiary engagement on telehealth\n##### (a) Resources, guidance, and training sessions\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) is amended by adding at the end the following new paragraph:\n(10) Resources, guidance, and training sessions (A) In general Not later than 6 months after the date of the enactment of this paragraph, the Secretary, in consultation with stakeholders, shall issue resources, guidance, and training sessions for beneficiaries, physicians, practitioners, and health information technology software vendors on best practices for ensuring telehealth services are accessible for\u2014 (i) individuals with limited English proficiency, including instructions on how to\u2014 (I) access telehealth platforms; (II) utilize interpreter services; and (III) integrate telehealth and virtual interpreter services; and (ii) individuals with disabilities, including instructions on accessibility of the telecommunications system being used for telehealth services, engagement with beneficiaries with disabilities prior to, during, and after the furnishing of the telehealth service, and training on captioning and transcripts. (B) Accounting for age and other differences Resources, guidance, and training sessions issued under this paragraph shall account for age and sociodemographic, geographic, literacy, cultural, cognitive, and linguistic differences in how individuals interact with technology. .\n##### (b) Study and report on tactics To improve beneficiary engagement on telehealth\n**(1) Study**\nThe Secretary of Health and Human Services shall, to the maximum extent feasible, collect and analyze qualitative and quantitative data on strategies that clinicians, payers, and other health care organizations use to improve beneficiary engagement on telehealth services (as defined in section 1834(m)(4)(F) of the Social Security Act ( 42 U.S.C. 1395m(m)(4)(F) )), with an emphasis on underserved communities, such as the use of digital navigators, providing patients with pre-visit information on telehealth, caregiver engagement, and training on telecommunications systems, and the investments necessary for health care professionals to effectively furnish telehealth services, including the costs of necessary technology and of training staff.\n**(2) Report**\nNot later than 2 years after the date of the enactment of this Act, the Secretary shall submit to Congress and make available on the internet website of the Secretary of Health and Human Services a report containing the results of the study under paragraph (1), together with recommendations for such legislation and administrative action as the Secretary determines appropriate.\n##### (c) Funding\nThere are authorized to be appropriated such sums as necessary to carry out the provisions of, including the amendments made by, this section.\n#### 302. Provider supports on telehealth\n##### (a) Educational resources and training sessions\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services shall develop and make available to health care professionals educational resources and training sessions on requirements relating to the furnishing of telehealth services under section 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) and topics including\u2014\n**(1)**\nrequirements for payment for telehealth services;\n**(2)**\ntelehealth-specific health care privacy and security training;\n**(3)**\nutilizing telehealth services to engage and support underserved, high-risk, and vulnerable patient populations; and\n**(4)**\nother topics as determined appropriate by the Secretary.\n##### (b) Funding\nThere are authorized to be appropriated such sums as necessary to carry out this section.\n#### 303. Ensuring the inclusion of telehealth in measuring quality of care\nSection 1890A of the Social Security Act ( 42 U.S.C. 1395aaa\u20131 ) is amended by adding at the end the following new subsection:\n(h) Measuring quality of telehealth services (1) In general Not later than 180 days after the date of the enactment of this subsection, the Secretary shall review quality measures to ensure inclusion of measures relating to telehealth services, including care, prevention, diagnosis, patient experience, health outcomes, and treatment. (2) Consultation In conducting the review and assessment under paragraph (1), the Secretary shall consult external technical experts in quality measurement, including patient organizations, providers, and experts in telehealth. (3) Review and assessment The review and assessment under this subsection shall\u2014 (A) include review of existing and under development quality measures to identify measures that are currently inclusive of, and measures that fail to account for, telehealth services; (B) identify gaps in areas of quality measurement that relate to telehealth services, including health outcomes and patient experience of care; and (C) assess how to effectively streamline, implement, and assign accountability for health outcomes for quality measures for telehealth services across health care settings and providers. (4) Technical guidance The Secretary shall issue technical guidance on the following for health care providers and other stakeholders, as determined appropriate by the Secretary: (A) How to stratify measures by care modality and population to identify differences in health outcomes. (B) The use of uniform data elements. (C) How to identify and catalogue best practices related to the use of quality measurement and quality improvement for telehealth services. (D) Other areas determined appropriate by the Secretary. (5) Report Not later than 2 years after the date of the enactment of this subsection, the Secretary shall submit to Congress and post on the internet website of the Centers for Medicare & Medicaid Services a report on the review and assessment conducted under this subsection. .\n#### 304. Posting of information on telehealth services\nNot later than 180 days after the date of the enactment of this Act, and quarterly thereafter, the Secretary of Health and Human Services shall post on the internet website of the Centers for Medicare & Medicaid Services information on\u2014\n**(1)**\nthe furnishing of telehealth services under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), described by patient population, type of service, geography, place of service, and provider type;\n**(2)**\nthe impact of telehealth services on expenditures and utilization under the Medicare program for the most recent 4 quarters for which Medicare claims data is available; and\n**(3)**\nother outcomes related to the furnishing of telehealth services under the Medicare program, as determined appropriate by the Secretary.",
      "versionDate": "2025-04-02",
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
        "actionDate": "2025-06-26",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4206",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CONNECT for Health Act of 2025",
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
        "updateDate": "2025-04-11T13:04:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-02",
    "originChamber": "Senate",
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
          "measure-id": "id119s1261",
          "measure-number": "1261",
          "measure-type": "s",
          "orig-publish-date": "2025-04-02",
          "originChamber": "SENATE",
          "update-date": "2026-05-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1261v00",
            "update-date": "2026-05-04"
          },
          "action-date": "2025-04-02",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Creating Opportunities Now for Necessary and Effective Care Technologies (CONNECT) for Health Act of 2025 or the CONNECT for Health Act of </strong><strong>2025</strong></p><p>This bill expands coverage of telehealth services under Medicare.</p><p>Among other provisions, the bill</p><ul><li>permanently removes geographic restrictions on originating sites (i.e., the location of the beneficiary) and allows the home of the beneficiary to serve as the originating site for all services;</li><li>permanently allows federally qualified health centers and rural health clinics to serve as the distant site (i.e., the location of the health care practitioner); and</li><li>allows the Centers for Medicare & Medicaid Services (CMS) to generally waive coverage restrictions during any public health emergency.</li></ul><p>Additionally, the CMS must post\u00a0certain information about the effects of Medicare telehealth services on its website, including information about utilization, costs, and the outcome of services.\u00a0The CMS must also (1) provide resources to health care professionals about\u00a0the requirements for furnishing telehealth services under Medicare, including with respect to payment, patient privacy, and support for underserved populations; and (2)\u00a0ensure certain quality measures are applied to telehealth services.</p>"
        },
        "title": "CONNECT for Health Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1261.xml",
    "summary": {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Opportunities Now for Necessary and Effective Care Technologies (CONNECT) for Health Act of 2025 or the CONNECT for Health Act of </strong><strong>2025</strong></p><p>This bill expands coverage of telehealth services under Medicare.</p><p>Among other provisions, the bill</p><ul><li>permanently removes geographic restrictions on originating sites (i.e., the location of the beneficiary) and allows the home of the beneficiary to serve as the originating site for all services;</li><li>permanently allows federally qualified health centers and rural health clinics to serve as the distant site (i.e., the location of the health care practitioner); and</li><li>allows the Centers for Medicare & Medicaid Services (CMS) to generally waive coverage restrictions during any public health emergency.</li></ul><p>Additionally, the CMS must post\u00a0certain information about the effects of Medicare telehealth services on its website, including information about utilization, costs, and the outcome of services.\u00a0The CMS must also (1) provide resources to health care professionals about\u00a0the requirements for furnishing telehealth services under Medicare, including with respect to payment, patient privacy, and support for underserved populations; and (2)\u00a0ensure certain quality measures are applied to telehealth services.</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119s1261"
    },
    "title": "CONNECT for Health Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Opportunities Now for Necessary and Effective Care Technologies (CONNECT) for Health Act of 2025 or the CONNECT for Health Act of </strong><strong>2025</strong></p><p>This bill expands coverage of telehealth services under Medicare.</p><p>Among other provisions, the bill</p><ul><li>permanently removes geographic restrictions on originating sites (i.e., the location of the beneficiary) and allows the home of the beneficiary to serve as the originating site for all services;</li><li>permanently allows federally qualified health centers and rural health clinics to serve as the distant site (i.e., the location of the health care practitioner); and</li><li>allows the Centers for Medicare & Medicaid Services (CMS) to generally waive coverage restrictions during any public health emergency.</li></ul><p>Additionally, the CMS must post\u00a0certain information about the effects of Medicare telehealth services on its website, including information about utilization, costs, and the outcome of services.\u00a0The CMS must also (1) provide resources to health care professionals about\u00a0the requirements for furnishing telehealth services under Medicare, including with respect to payment, patient privacy, and support for underserved populations; and (2)\u00a0ensure certain quality measures are applied to telehealth services.</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119s1261"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1261is.xml"
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
      "title": "CONNECT for Health Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CONNECT for Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Opportunities Now for Necessary and Effective Care Technologies (CONNECT) for Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to expand access to telehealth services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:38Z"
    }
  ]
}
```
