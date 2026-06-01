# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1241?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1241
- Title: Sanctioning Russia Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1241
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-01-10T06:45:10Z
- Update date including text: 2026-01-10T06:45:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1241",
    "number": "1241",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Sanctioning Russia Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T06:45:10Z",
    "updateDateIncludingText": "2026-01-10T06:45:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
        "item": {
          "date": "2025-04-01T21:44:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AK"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "IL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AL"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "RI"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "IN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-01",
      "state": "ME"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NE"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "VA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "ND"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "UT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "HI"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AR"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NH"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NE"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "IA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "HI"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MS"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NH"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NC"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "VT"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "OK"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "DE"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NY"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AK"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "OH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MI"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "IA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CO"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CO"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "ND"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "PA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "OK"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NM"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MT"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "RI"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "LA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WY"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NV"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "OR"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "GA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "ME"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "MS"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "WI"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "LA"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "WA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NM"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "SD"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "AL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "PA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "ID"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "ID"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "WY"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "KY"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "TX"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "MI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "WA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "VA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "DE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "SD"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "KS"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "IL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TN"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1241is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1241\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Graham (for himself, Mr. Blumenthal , Mr. Sullivan , Mr. Durbin , Mrs. Britt , Mr. Whitehouse , Mr. Young , Mr. King , Mr. Ricketts , Mr. Kaine , Mr. Cramer , Ms. Klobuchar , Mr. Curtis , Mr. Schatz , Mr. Cotton , Ms. Hassan , Mrs. Fischer , Ms. Alsobrooks , Ms. Ernst , Ms. Hirono , Mr. Wicker , Mrs. Shaheen , Mr. Tillis , Mr. Welch , Mr. Mullin , Mr. Coons , Mr. Sheehy , Mrs. Gillibrand , Ms. Murkowski , Mr. Kelly , Mr. Husted , Ms. Slotkin , Mr. Grassley , Mr. Hickenlooper , Mr. Cornyn , Mr. Bennet , Mrs. Capito , Mr. Gallego , Mr. Hoeven , Mr. Fetterman , Mr. Boozman , Mr. Van Hollen , Mr. Lankford , Mr. Heinrich , Mr. Scott of Florida , Mr. Schiff , Mr. Justice , Ms. Warren , Mr. Daines , Mr. Reed , Mr. Kennedy , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo impose sanctions and other measures with respect to the Russian Federation if the Government of the Russian Federation refuses to negotiate a peace agreement with Ukraine, violates any such agreement, or initiates another military invasion of Ukraine, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Sanctioning Russia Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Sense of Congress.\nSec. 3. Definitions.\nSec. 4. Covered determination.\nSec. 5. Imposition of sanctions on certain persons affiliated with or supporting the Government of the Russian Federation.\nSec. 6. Imposition of sanctions with respect to financial institutions affiliated with the Government of the Russian Federation.\nSec. 7. Imposition of sanctions with respect to other entities owned by or affiliated with the Government of the Russian Federation.\nSec. 8. Prohibition on transfers of funds involving the Russian Federation.\nSec. 9. Prohibition on listing or trading of Russian entities on United States securities exchanges.\nSec. 10. Prohibition on investments by United States financial institutions that benefit the Government of the Russian Federation.\nSec. 11. Prohibition on energy exports to, and investments in energy sector of, the Russian Federation.\nSec. 12. Prohibition on purchases of sovereign debt of the Russian Federation by United States persons.\nSec. 13. Prohibition on provision of services to sanctioned financial institutions by international financial messaging systems.\nSec. 14. Prohibition on importing, and sanctions with respect to, uranium from the Russian Federation.\nSec. 15. Increases in duties on goods and services imported from the Russian Federation.\nSec. 16. Imposition of CAATSA sanctions.\nSec. 17. Duties on countries that purchase Russian-origin oil, uranium, and petroleum products.\nSec. 18. Exceptions.\nSec. 19. Implementation; penalties.\nSec. 20. Termination authority; reimposition of sanctions.\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nif the Government of the Russian Federation is refusing to engage in good faith negotiations for a lasting peace with Ukraine, the Russian Federation should be subject to maximum sanctions as allowed under United States law; and\n**(2)**\nin order to prevent another military invasion or act that undermines the sovereignty of Ukraine following a negotiated peace, it should be the policy of the United States to provide sustainable levels of security assistance to Ukraine to provide a credible defensive and deterrent capability.\n#### 3. Definitions\nIn this Act:\n**(1) Account; correspondent account; payable-through account**\nThe terms account , correspondent account , and payable-through account have the meanings given those terms in section 5318A of title 31, United States Code.\n**(2) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(3) Armed Forces of the Russian Federation**\nThe term Armed Forces of the Russian Federation includes\u2014\n**(A)**\nthe Aerospace Forces of the Russian Federation;\n**(B)**\nthe Airborne Forces of the Russian Federation;\n**(C)**\nthe Ground Forces of the Russian Federation;\n**(D)**\nthe Navy of the Russian Federation;\n**(E)**\nthe Special Operations Command of the Russian Federation;\n**(F)**\nthe Strategic Rocket Forces of the Russian Federation;\n**(G)**\nthe General Staff of the Armed Forces of the Russian Federation;\n**(H)**\nthe Main Directorate of the General Staff of the Armed Forces of the Russian Federation; and\n**(I)**\nany successor entities or proxies of the entities described in subparagraphs (A) through (H).\n**(4) Covered determination**\nThe term covered determination means a determination by the President as described in section 4.\n**(5) Critical infrastructure**\n**(A) In general**\nThe term critical infrastructure , with respect to Ukraine, means systems and assets, whether physical or virtual, so vital to Ukraine that the incapacity or destruction of such systems and assets would have catastrophic regional or national effects on public health or safety, economic security, or national security.\n**(B) Included sectors**\nThe term critical infrastructure includes assets in the following sectors:\n**(i)**\nBiotechnology.\n**(ii)**\nChemical.\n**(iii)**\nCommercial facilities.\n**(iv)**\nCommunications.\n**(v)**\nCritical manufacturing.\n**(vi)**\nDams.\n**(vii)**\nDefense industrial base.\n**(viii)**\nEmergency services.\n**(ix)**\nEnergy.\n**(x)**\nFinancial services.\n**(xi)**\nFood and agriculture.\n**(xii)**\nGovernment facilities.\n**(xiii)**\nHealthcare and public health.\n**(xiv)**\nInformation technology.\n**(xv)**\nMaterials and waste.\n**(xvi)**\nNuclear reactors.\n**(xvii)**\nSpace.\n**(xviii)**\nTransportation systems.\n**(xix)**\nWater and wastewater systems.\n**(6) Financial institution**\nThe term financial institution means a financial institution specified in subparagraph (A), (B), (C), (D), (E), (F), (G), (H), (I), (J), (M), or (Y) of section 5312(a)(2) of title 31, United States Code.\n**(7) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(8) Knowingly; knows**\nThe terms knowingly and knows , with respect to conduct, a circumstance, or a result, means that a person had actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(9) Military invasion**\nThe term military invasion includes\u2014\n**(A)**\na ground operation or assault;\n**(B)**\nan amphibious landing or assault;\n**(C)**\nan airborne operation or air assault;\n**(D)**\nan aerial bombardment or blockade;\n**(E)**\nmissile attacks, including rockets, ballistic missiles, cruise missiles, and hypersonic missiles;\n**(F)**\na naval bombardment or armed blockade;\n**(G)**\na cyber attack; and\n**(H)**\nan attack by a country on any territory controlled or administered by any other independent, sovereign country, including offshore islands controlled or administered by that country.\n**(10) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity.\n#### 4. Covered determination\n##### (a) In general\nNot later than 15 days after the date of the enactment of this Act, and every 90 days thereafter, the President shall determine if any of the following actors has engaged, is engaging, or is planning to engage in an act described in subsection (b):\n**(1)**\nThe Government of the Russian Federation.\n**(2)**\nAny proxy of the Government of the Russian Federation.\n**(3)**\nAny individual or entity controlled by or acting at the direction of the Government of the Russian Federation.\n**(4)**\nAny person described in section 5 or 6.\n##### (b) Acts described\nAn act described in this subsection is any of the following:\n**(1)**\nRefusing to negotiate a peace agreement with Ukraine.\n**(2)**\nViolating any negotiated peace agreement.\n**(3)**\nInitiating another military invasion of Ukraine.\n**(4)**\nOverthrowing, dismantling, or seeking to subvert the Government of Ukraine.\n#### 5. Imposition of sanctions on certain persons affiliated with or supporting the Government of the Russian Federation\n##### (a) In general\nNot later than 15 days after making a covered determination, and every 90 days thereafter, the President shall\u2014\n**(1)**\nimpose the sanctions described in subsection (c) with respect to the persons described in subsection (b); and\n**(2)**\nprohibit any United States person from engaging in any transaction with a person described in subsection (b).\n##### (b) Persons described\nThe persons described in this subsection are the following:\n**(1)**\nThe following officials of the Government of the Russian Federation:\n**(A)**\nThe President of the Russian Federation.\n**(B)**\nThe Prime Minister of the Russian Federation.\n**(C)**\nThe Minister of Defense of the Russian Federation.\n**(D)**\nThe Chief of the General Staff of the Armed Forces of the Russian Federation.\n**(E)**\nThe Deputy Ministers of Defense of the Russian Federation.\n**(F)**\nThe Commander-in-Chief of the Land Forces of the Russian Federation.\n**(G)**\nThe Commander-in-Chief of the Aerospace Forces of the Russian Federation.\n**(H)**\nThe Commander of the Airborne Forces of the Russian Federation.\n**(I)**\nThe Commander-in-Chief of the Navy of the Russian Federation.\n**(J)**\nThe Commander of the Strategic Rocket Forces of the Russian Federation.\n**(K)**\nThe Commander of the Special Operations Forces of the Russian Federation.\n**(L)**\nThe Commander of Logistical Support of the Armed Forces of the Russian Federation.\n**(M)**\nThe commanders of the Russian Federation military districts.\n**(N)**\nThe Minister of Foreign Affairs of the Russian Federation.\n**(O)**\nThe Minister of Transport of the Russian Federation.\n**(P)**\nThe Minister of Finance of the Russian Federation.\n**(Q)**\nThe Minister of Industry and Trade of the Russian Federation.\n**(R)**\nThe Minister of Energy of the Russian Federation.\n**(S)**\nThe Minister of Agriculture of the Russian Federation.\n**(T)**\nThe Director of the Foreign Intelligence Service of the Russian Federation.\n**(U)**\nThe Director of the Federal Security Service of the Russian Federation.\n**(V)**\nThe Director of the Main Directorate of the General Staff of the Armed Forces of the Russian Federation.\n**(W)**\nThe Director of the National Guard of the Russian Federation.\n**(X)**\nThe Federal Guard Service of the Russian Federation.\n**(2)**\nAny foreign person that\u2014\n**(A)**\nknowingly sells, supplies, transfers, markets, or provides defense articles, equipment, goods, services, technology, or materials to the Armed Forces of the Russian Federation;\n**(B)**\nknowingly conducts a transaction with the Armed Forces of the Russian Federation;\n**(C)**\nhas engaged in or attempted to engage in activities that\u2014\n**(i)**\nmaterially undermine the military readiness of Ukraine;\n**(ii)**\nseek to overthrow, dismantle, or subvert the Government of Ukraine;\n**(iii)**\ndebilitate the critical infrastructure of Ukraine;\n**(iv)**\ndebilitate cybersecurity systems through malicious electronic attacks or cyberattacks on Ukraine;\n**(v)**\nundermine the democratic processes of Ukraine; or\n**(vi)**\ninvolve committing serious human rights abuses against citizens of Ukraine, including forceful transfers, enforced disappearances, unjust detainment, or torture;\n**(D)**\noperates or has operated in the energy, commodities, telecommunications, banking, industrial, transportation, or manufacturing sectors of the economy of the Russian Federation;\n**(E)**\nis an oligarch (as defined and identified by the President);\n**(F)**\nis responsible for or complicit in, or has directly or indirectly engaged or attempted to engage in, for or on behalf of, or for the benefit of, directly or indirectly, the Government of the Russian Federation\u2014\n**(i)**\ntransnational corruption, bribery, extortion, or money laundering;\n**(ii)**\nassassination, murder, or other unlawful killing of, or infliction of other bodily harm against, a United States person or a citizen or national of an ally or partner of the United States;\n**(iii)**\nactivities that undermine the peace, security, political stability, or territorial integrity of the United States or an ally or partner of the United States; or\n**(iv)**\ndeceptive or structured transactions or dealings to circumvent the application of any sanctions imposed by the United States, including through the use of digital currencies or assets or the use of physical assets.\n**(3)**\nAny person or agent of any person described in paragraph (1) or (2) if the sanctioned person transferred property or an interest in property to the person\u2014\n**(A)**\nafter the date on which the President imposed sanctions with respect to the sanctioned person; or\n**(B)**\nbefore that date, if the sanctioned person did so in an attempt to evade the imposition of sanctions.\n##### (c) Sanctions described\nThe sanctions described in this subsection to be imposed with respect to a person described in subsection (b) are the following:\n**(1) Blocking of property**\n**(A) In general**\nThe President shall exercise all of the powers granted by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to block and prohibit all transactions in all property and interests in property of the person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(B) Inapplicability of national emergency requirement**\nThe requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ) shall not apply for purposes of this section.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien described in subsection (b) shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subsection (b) shall be revoked, regardless of when such visa or other entry documentation is or was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n#### 6. Imposition of sanctions with respect to financial institutions affiliated with the Government of the Russian Federation\n##### (a) In general\nNot later than 15 days after making a covered determination, and every 90 days thereafter, the Secretary of the Treasury shall\u2014\n**(1)**\nimpose the sanctions described in subsection (b) with respect to\u2014\n**(A)**\nthe Central Bank of the Russian Federation (Bank of Russia);\n**(B)**\nSberbank;\n**(C)**\nVTB Bank;\n**(D)**\nGazprombank;\n**(E)**\nany other financial institution organized under the laws of the Russian Federation and owned in whole or part by the Government of the Russian Federation;\n**(F)**\nany subsidiary of, or successor entity to, any of the financial institutions described in subparagraphs (A) through (E); and\n**(G)**\nany financial institution that engages in transactions with any of the financial institutions described in subparagraphs (A) through (F);\n**(2)**\nimpose the sanctions described in section 5(c) with respect to any directors of, officers of, officials of, and shareholders with an interest in, a financial institution described in paragraph (1); and\n**(3)**\nprohibit any United States person from engaging in any transaction with a financial institution described in paragraph (1).\n##### (b) Sanctions described\nThe sanctions described in this subsection to be imposed with respect to a financial institution described in subsection (a)(1) are the following:\n**(1) Blocking of property**\n**(A) In general**\nThe President shall exercise all of the powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in property and interests in property of the financial institution if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(B) Inapplicability of national emergency requirement**\nThe requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ) shall not apply for purposes of this section.\n**(2) Restrictions on correspondent and payable-through accounts**\nThe President shall prohibit the opening, and prohibit or impose strict conditions on the maintaining, in the United States, of a correspondent account or payable-through account by the financial institution.\n#### 7. Imposition of sanctions with respect to other entities owned by or affiliated with the Government of the Russian Federation\n##### (a) In general\nNot later than 15 days after making a covered determination, and every 90 days thereafter, the Secretary of the Treasury shall impose the sanctions described in subsection (b) with respect to any entity that\u2014\n**(1)**\nthe Government of the Russian Federation has an ownership interest in; or\n**(2)**\nis otherwise affiliated with the Government of the Russian Federation.\n##### (b) Blocking of property\n**(1) In general**\nThe President shall exercise all of the powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in property and interests in property of an entity described in subsection (a) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Inapplicability of national emergency requirement**\nThe requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ) shall not apply for purposes of this section.\n#### 8. Prohibition on transfers of funds involving the Russian Federation\n##### (a) In general\nExcept as provided by subsection (b), not later than 15 days after a covered determination is made, a depository institution (as defined in section 19(b)(1)(A) of the Federal Reserve Act ( 12 U.S.C. 461(b)(1)(A) )) or a broker or dealer in securities registered with the Securities and Exchange Commission under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. ) may not process transfers of funds\u2014\n**(1)**\nto or from the Russian Federation; or\n**(2)**\nfor the direct or indirect benefit of officials of the Government of the Russian Federation.\n##### (b) Exception\nA depository institution, broker, or dealer described in subsection (a) may process a transfer described in that subsection if the transfer\u2014\n**(1)**\narises from, and is ordinarily incident and necessary to give effect to, an underlying transaction that is authorized by a specific or general license; and\n**(2)**\ndoes not involve debiting or crediting an account affiliated with the Russian Federation or held by a Russian person.\n##### (c) Russian person defined\nIn this section, the term Russian person means\u2014\n**(1)**\na citizen or national of the Russian Federation; or\n**(2)**\nan entity organized under the laws of the Russian Federation or otherwise subject to the jurisdiction of the Government of the Russian Federation.\n#### 9. Prohibition on listing or trading of Russian entities on United States securities exchanges\n##### (a) In general\nNot later than 15 days after a covered determination is made, the Securities and Exchange Commission shall prohibit the securities of an issuer described in subsection (b) from being traded on a national securities exchange.\n##### (b) Issuers\nAn issuer described in this subsection is an issuer that is\u2014\n**(1)**\nan official of or individual affiliated with the Government of the Russian Federation; or\n**(2)**\nan entity that\u2014\n**(A)**\nthe Government of the Russian Federation has an ownership interest in; or\n**(B)**\nis otherwise affiliated with the Government of the Russian Federation.\n##### (c) Definitions\nIn this section:\n**(1) Issuer; security**\nThe terms issuer and security have the meanings given those terms in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ).\n**(2) National securities exchange**\nThe term national securities exchange means an exchange registered as a national securities exchange in accordance with section 6 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f ).\n#### 10. Prohibition on investments by United States financial institutions that benefit the Government of the Russian Federation\n##### (a) In general\nNot later than 15 days after a covered determination is made, the Secretary of the Treasury shall prohibit any United States financial institution from making any investment described in subsection (b).\n##### (b) Investments described\nAn investment described in this subsection is a monetary investment in or to\u2014\n**(1)**\nan entity owned or controlled by the Government of the Russian Federation; or\n**(2)**\nthe Armed Forces of the Russian Federation.\n##### (c) United states financial institution defined\nIn this section, the term United States financial institution \u2014\n**(1)**\nmeans any financial institution that is a United States person; and\n**(2)**\nincludes an investment company, private equity company, venture capital company, or hedge fund that is a United States person.\n#### 11. Prohibition on energy exports to, and investments in energy sector of, the Russian Federation\n##### (a) Prohibition on exports\n**(1) In general**\nNot later than 15 days after a covered determination is made, the Secretary of Commerce shall prohibit, under the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ), the export, reexport, or in-country transfer to or in the Russian Federation of any energy or energy product produced in the United States.\n**(2) Definitions**\nIn this subsection, the terms export , in-country transfer , and reexport have the meanings given those terms in section 1742 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 ).\n##### (b) Prohibition on investments\nOn and after the date on which a covered determination is made, a United States person may not make an investment in the energy sector of the Russian Federation.\n##### (c) Sanctions\nThe President shall\u2014\n**(1)**\nimpose the sanctions described in section 5(c) with respect to any foreign person that the President determines knowingly sells, supplies, transfers, markets, or provides goods, services, technology, information, or other support that facilitates the maintenance or expansion of the production of oil, uranium, natural gas, petroleum, petroleum products, or petrochemical products for use by any person subject to sanctions under section 5 or 6; and\n**(2)**\nprohibit any United States person from engaging in any transaction with a person described in paragraph (1).\n#### 12. Prohibition on purchases of sovereign debt of the Russian Federation by United States persons\nOn and after the date that is 15 days after a covered determination is made, the purchase of sovereign debt of the Government of the Russian Federation by any United States person is prohibited.\n#### 13. Prohibition on provision of services to sanctioned financial institutions by international financial messaging systems\nNot later than 15 days after making a covered determination, and every 90 days thereafter, the President shall impose sanctions pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) with respect to\u2014\n**(1)**\nany global financial communications services provider that does not terminate the provision of financial communications services to, and the enabling and facilitation of access to such services for, any financial institution subject to sanctions under section 6 or any other provision of this Act; and\n**(2)**\nthe directors of, officers of, and shareholders with a interest in, the provider.\n#### 14. Prohibition on importing, and sanctions with respect to, uranium from the Russian Federation\n##### (a) Prohibition\nNot later than 15 days after making a covered determination, the President shall prohibit the importation of uranium from\u2014\n**(1)**\nthe Russian Federation, including the importation of any uranium from Rosatom State Corporation or any subsidiary or successor entity; and\n**(2)**\nany country that has uranium that was originally sourced from the Russian Federation, Rosatom State Corporation, or any subsidiary or successor entity.\n##### (b) Sanctions\nNot later than 15 days after making a covered determination, and every 90 days thereafter, the President shall impose sanctions described in section 5(c) with respect to\u2014\n**(1)**\nany directors of, officers of, and shareholders with an interest in, Rosatom State Corporation or any subsidiary or successor entity; and\n**(2)**\nany foreign government or foreign person that has knowingly sold, supplied, transferred, or purchased uranium originally sourced from the Russian Federation, Rosatom State Corporation, or any subsidiary or successor entity.\n#### 15. Increases in duties on goods and services imported from the Russian Federation\n##### (a) In general\nNot later than 15 days after making a covered determination, the President shall, notwithstanding any other provision of law, increase the rate of duty for all goods and services, including oil, natural gas, petroleum, petroleum products, and petrochemical products, imported into the United States from the Russian Federation to a rate of not less than the equivalent of 500 percent ad valorem.\n##### (b) Recommendations for higher rate\nThe United States Trade Representative, in consultation with the Secretary of the Treasury, the Secretary of Commerce, and the heads of other relevant Federal agencies, shall provide recommendations to the President with respect to goods and services described in subsection (a) that should be subject to a rate of duty that exceeds the equivalent of 500 percent ad valorem.\n##### (c) Duty rate in addition to antidumping and countervailing duties\nThe rate of duty required under subsection (a) with respect to a good or service described in that subsection shall be in addition to any antidumping or countervailing duty applicable with respect to the good or service under title VII of the Tariff Act of 1930 ( 19 U.S.C. 1671 et seq. ).\n#### 16. Imposition of CAATSA sanctions\nNot later than 15 days after making a covered determination, and every 90 days thereafter, the President shall impose all sanctions described in section 235 of the Countering America\u2019s Adversaries Through Sanctions Act ( 22 U.S.C. 9529 ) that are not already applicable with respect to\u2014\n**(1)**\nthe Russian Federation; and\n**(2)**\nany person described in section 5 or 6.\n#### 17. Duties on countries that purchase Russian-origin oil, uranium, and petroleum products\n##### (a) In general\nNot later than 15 days after making a covered determination, and every 90 days thereafter, the President shall, notwithstanding any other provision of law, increase the rate of duty for all goods or services imported into the United States from a country described in subsection (b) to a rate of not less than the equivalent of 500 percent ad valorem.\n##### (b) Countries described\nA country is described in this subsection if the country knowingly sells, supplies, transfers, or purchases oil, uranium, natural gas, petroleum products, or petrochemical products that originated in the Russian Federation.\n##### (c) Duty rate in addition to antidumping and countervailing duties\nThe rate of duty required under subsection (a) with respect to a good or service described in that subsection shall be in addition to any antidumping or countervailing duty applicable with respect to the good or service under title VII of the Tariff Act of 1930 ( 19 U.S.C. 1671 et seq. ).\n##### (d) Waiver\n**(1) In general**\nThe President may waive the application of subsection (a) one time for a period of not more than 180 days with respect to a country, a good, or a service if the President determines that such a waiver is in the national security interests of the United States.\n**(2) Prohibition on waivers for certain countries**\nThe President may not waive the application of subsection (a) with respect to\u2014\n**(A)**\na country the government of which the Secretary of State has determined has repeatedly provided support for acts of international terrorism (commonly referred to as a state sponsor of terrorism ), for purposes of\u2014\n**(i)**\nsection 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) );\n**(ii)**\nsection 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 );\n**(iii)**\nsection 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) ); or\n**(iv)**\nany other provision of law; or\n**(B)**\na country specified in section 4872(f)(2) of title 10, United States Code.\n#### 18. Exceptions\n##### (a) Support for people of the Russian Federation\nThis Act shall not apply with respect to the provision of humanitarian assistance (including medical assistance) to the people of the Russian Federation.\n##### (b) Exception for intelligence activities\nThis Act shall not apply with respect to activities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States.\n##### (c) Exception To comply with international obligations\nSanctions under this Act shall not apply to the admission of an alien if the admission of that alien is necessary to comply with United States obligations under the Agreement between the United Nations and the United States of America regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, under the Convention on Consular Relations, done at Vienna April 24, 1963, and entered into force March 19, 1967, or under other international agreements.\n#### 19. Implementation; penalties\n##### (a) Implementation\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this Act.\n##### (b) Penalties\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this Act or any regulation, license, or order issued to carry out this Act shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n#### 20. Termination authority; reimposition of sanctions\n##### (a) In general\nThe President may terminate the application of sanctions, prohibitions, restrictions, duties, and penalties under this Act if the President certifies to Congress that\u2014\n**(1)**\nall actors described in subsection (a) of section 4 have verifiably ceased engaging in acts described in subsection (b) of that section; and\n**(2)**\nthe Government of the Russian Federation has entered into a peace agreement with Ukraine.\n##### (b) Reimposition\nIf, after the submission of a certification described in subsection (a), an actor described in subsection (a) of section 4 engages in an act described in subsection (b) of that section, the President shall immediately reimpose all previously terminated sanctions, prohibitions, restrictions, duties, and penalties imposed under this Act, in addition to new sanctions, prohibitions, restrictions, duties, and penalties under this Act.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-12-11",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6636",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance sensible priorities.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-01",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on the Judiciary, Financial Services, Ways and Means, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2548",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Sanctioning Russia Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-05-23T13:26:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119s1241",
          "measure-number": "1241",
          "measure-type": "s",
          "orig-publish-date": "2025-04-01",
          "originChamber": "SENATE",
          "update-date": "2025-07-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1241v00",
            "update-date": "2025-07-15"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Sanctioning Russia Act of 2025</strong><br/>\u00a0<br/>This bill imposes penalties on certain persons (individuals and entities) if the President determines that the Russian government or a person acting at Russia's direction is involved with (1) refusing to negotiate a peace agreement with Ukraine; (2) violating a negotiated peace agreement; (3) initiating another invasion of Ukraine; or (4) overthrowing, dismantling, or seeking to subvert the Ukrainian government.<br/>\u00a0<br/>If the President makes such a determination, the bill requires certain actions including</p><ul><li>the President must impose visa- and property-blocking sanctions on specified persons such as the Russian president, certain Russian military commanders, and any foreign person that knowingly provides defense items to the Russian armed forces;</li><li>the President must increase the rate of duty on all goods and services imported from Russia into the United States to at least 500% relative to the value of such goods and services;</li><li>the President must increase the rate of duty on all goods and services imported into the United States from countries that knowingly engage in the exchange of Russian-origin uranium and petroleum products to at least 500% relative to the value of such goods and services;</li><li>the Department of the Treasury must impose property-blocking sanctions on any financial institution organized under Russian law and owned wholly or partly by Russia, and any financial institution that engages in transactions with those entities; and</li><li>the Department of Commerce must prohibit the export, reexport, or in-country transfer to or in Russia of any U.S.-produced energy or energy product.</li></ul>"
        },
        "title": "Sanctioning Russia Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1241.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sanctioning Russia Act of 2025</strong><br/>\u00a0<br/>This bill imposes penalties on certain persons (individuals and entities) if the President determines that the Russian government or a person acting at Russia's direction is involved with (1) refusing to negotiate a peace agreement with Ukraine; (2) violating a negotiated peace agreement; (3) initiating another invasion of Ukraine; or (4) overthrowing, dismantling, or seeking to subvert the Ukrainian government.<br/>\u00a0<br/>If the President makes such a determination, the bill requires certain actions including</p><ul><li>the President must impose visa- and property-blocking sanctions on specified persons such as the Russian president, certain Russian military commanders, and any foreign person that knowingly provides defense items to the Russian armed forces;</li><li>the President must increase the rate of duty on all goods and services imported from Russia into the United States to at least 500% relative to the value of such goods and services;</li><li>the President must increase the rate of duty on all goods and services imported into the United States from countries that knowingly engage in the exchange of Russian-origin uranium and petroleum products to at least 500% relative to the value of such goods and services;</li><li>the Department of the Treasury must impose property-blocking sanctions on any financial institution organized under Russian law and owned wholly or partly by Russia, and any financial institution that engages in transactions with those entities; and</li><li>the Department of Commerce must prohibit the export, reexport, or in-country transfer to or in Russia of any U.S.-produced energy or energy product.</li></ul>",
      "updateDate": "2025-07-15",
      "versionCode": "id119s1241"
    },
    "title": "Sanctioning Russia Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sanctioning Russia Act of 2025</strong><br/>\u00a0<br/>This bill imposes penalties on certain persons (individuals and entities) if the President determines that the Russian government or a person acting at Russia's direction is involved with (1) refusing to negotiate a peace agreement with Ukraine; (2) violating a negotiated peace agreement; (3) initiating another invasion of Ukraine; or (4) overthrowing, dismantling, or seeking to subvert the Ukrainian government.<br/>\u00a0<br/>If the President makes such a determination, the bill requires certain actions including</p><ul><li>the President must impose visa- and property-blocking sanctions on specified persons such as the Russian president, certain Russian military commanders, and any foreign person that knowingly provides defense items to the Russian armed forces;</li><li>the President must increase the rate of duty on all goods and services imported from Russia into the United States to at least 500% relative to the value of such goods and services;</li><li>the President must increase the rate of duty on all goods and services imported into the United States from countries that knowingly engage in the exchange of Russian-origin uranium and petroleum products to at least 500% relative to the value of such goods and services;</li><li>the Department of the Treasury must impose property-blocking sanctions on any financial institution organized under Russian law and owned wholly or partly by Russia, and any financial institution that engages in transactions with those entities; and</li><li>the Department of Commerce must prohibit the export, reexport, or in-country transfer to or in Russia of any U.S.-produced energy or energy product.</li></ul>",
      "updateDate": "2025-07-15",
      "versionCode": "id119s1241"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1241is.xml"
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
      "title": "Sanctioning Russia Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sanctioning Russia Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose sanctions and other measures with respect to the Russian Federation if the Government of the Russian Federation refuses to negotiate a peace agreement with Ukraine, violates any such agreement, or initiates another military invasion of Ukraine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:35Z"
    }
  ]
}
```
