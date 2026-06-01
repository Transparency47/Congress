# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1748?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1748
- Title: Kids Online Safety Act
- Congress: 119
- Bill type: S
- Bill number: 1748
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2026-02-04T12:03:15Z
- Update date including text: 2026-02-04T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S2929-2930)
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S2929-2930)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1748",
    "number": "1748",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Kids Online Safety Act",
    "type": "S",
    "updateDate": "2026-02-04T12:03:15Z",
    "updateDateIncludingText": "2026-02-04T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S2929-2930)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-14",
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
            "date": "2025-05-14T15:47:13Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-14T15:47:13Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sponsorshipDate": "2025-05-14",
      "state": "CT"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "SD"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CO"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "AZ"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NM"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "KS"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "ID"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "FL"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "ND"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "WV"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MS"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NM"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "TX"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "NE"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "AK"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "AK"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "IA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "ME"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "VT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "OK"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "IN"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "IA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "GA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "IL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "AL"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NH"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "RI"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "IN"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "LA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "UT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "MS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "FL"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "RI"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "OK"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "WY"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "LA"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "SC"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ID"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "PA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "DE"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "TN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-10-09",
      "state": "ME"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "HI"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "OH"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "VA"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "MO"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ND"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "AL"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "IL"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "OH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "MD"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "MI"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NE"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "AZ"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "AR"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CO"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "AR"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "DE"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "WY"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1748is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1748\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mrs. Blackburn (for herself, Mr. Blumenthal , Mr. Thune , and Mr. Schumer ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo protect the safety of children on the internet.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Kids Online Safety Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Kids Online Safety\nSec. 101. Definitions.\nSec. 102. Duty of care.\nSec. 103. Safeguards for minors.\nSec. 104. Disclosure.\nSec. 105. Transparency.\nSec. 106. Market research.\nSec. 107. Age verification study and report.\nSec. 108. Guidance.\nSec. 109. Enforcement.\nSec. 110. Kids online safety council.\nSec. 111. Effective date.\nSec. 112. Rules of construction and other matters.\nTITLE II\u2014Filter Bubble Transparency\nSec. 201. Definitions.\nSec. 202. Requirement to allow users to see unmanipulated content on internet platforms.\nTITLE III\u2014Relationship to State laws; severability\nSec. 301. Relationship to State laws.\nSec. 302. Severability.\nI\nKids Online Safety\n#### 101. Definitions\nIn this title:\n**(1) Child**\nThe term child means an individual who is under the age of 13.\n**(2) Compulsive usage**\nThe term compulsive usage means a persistent and repetitive use of a covered platform that significantly impacts one or more major life activities of an individual, including socializing, sleeping, eating, learning, reading, concentrating, communicating, or working.\n**(3) Covered platform**\n**(A) In general**\nThe term covered platform means an online platform, online video game, messaging application, or video streaming service that connects to the internet and that is used, or is reasonably likely to be used, by a minor.\n**(B) Exceptions**\nThe term covered platform does not include\u2014\n**(i)**\nan entity acting in its capacity as a provider of\u2014\n**(I)**\na common carrier service subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) and all Acts amendatory thereof and supplementary thereto;\n**(II)**\na broadband internet access service (as such term is defined for purposes of section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation);\n**(III)**\nan email service;\n**(IV)**\na teleconferencing or video conferencing service that allows reception and transmission of audio or video signals for real-time communication, provided that\u2014\n**(aa)**\nthe service is not an online platform; and\n**(bb)**\nthe real-time communication is initiated by using a unique link or identifier to facilitate access; or\n**(V)**\na wireless messaging service, including such a service provided through short messaging service or multimedia messaging service protocols, that is not a component of, or linked to, an online platform and where the predominant or exclusive function is direct messaging consisting of the transmission of text, photos or videos that are sent by electronic means, where messages are transmitted from the sender to a recipient, and are not posted within an online platform or publicly;\n**(ii)**\nan organization not organized to carry on business for its own profit or that of its members;\n**(iii)**\nany public or private\u2014\n**(I)**\nearly childhood education program or preschool that provides for the care, development, and education of infants, toddlers, or young children who are not yet enrolled in kindergarten;\n**(II)**\nelementary school (as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )) or secondary school (as so defined);\n**(III)**\nschool providing career and technical education (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ));\n**(IV)**\nschool providing adult education and literacy activities (as defined in section 203 of the Adult Education and Family Literacy Act ( 29 U.S.C. 3272 )); or\n**(V)**\ninstitution of higher education (as defined in section 101, and subparagraphs (A) and (B) of section 102(a)(1), of the Higher Education Act of 1965 ( 20 U.S.C. 1001 , 1002(a)(1)));\n**(iv)**\na library (as defined in section 213 of the Library Services and Technology Act ( 20 U.S.C. 9122 ));\n**(v)**\na news or sports coverage website or app where\u2014\n**(I)**\nthe inclusion of video content on the website or app is related to the website or app\u2019s own gathering, reporting, or publishing of news content or sports coverage; and\n**(II)**\nthe website or app is not otherwise an online platform;\n**(vi)**\na product or service that primarily functions as business-to-business software, such as a cloud storage, file sharing, or file collaboration service;\n**(vii)**\na virtual private network or similar service that exists predominantly to route internet traffic between locations; or\n**(viii)**\na government entity with a .gov internet domain (as described in section 2215 of the Homeland Security Act of 2002 ( 6 U.S.C. 665 )).\n**(4) Design feature**\nThe term design feature means any feature or component of a covered platform that will encourage or increase the frequency, time spent, or activity of minors on the covered platform. Design features include but are not limited to\u2014\n**(A)**\ninfinite scrolling or auto play;\n**(B)**\nrewards or incentives based on the frequency, time spent, or activity of minors on the covered platform;\n**(C)**\nnotifications and push alerts;\n**(D)**\nbadges or other visual award symbols based on the frequency, time spent, or activity of minors on the covered platform;\n**(E)**\npersonalized design features;\n**(F)**\nin-game purchases; or\n**(G)**\nappearance altering filters.\n**(5) Geolocation**\nThe term geolocation has the meaning given the term geolocation information in section 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ), as added by section 201(a).\n**(6) Know or knows**\nThe term know or knows means to have actual knowledge or knowledge fairly implied on the basis of objective circumstances.\n**(7) Microtransaction**\n**(A) In general**\nThe term microtransaction means a purchase made in an online video game (including a purchase made using a virtual currency that is purchasable or redeemable using cash or credit or that is included as part of a paid subscription service).\n**(B) Inclusions**\nSuch term includes a purchase involving surprise mechanics, new characters, or in-game items.\n**(C) Exclusions**\nSuch term does not include\u2014\n**(i)**\na purchase made in an online video game using a virtual currency that is earned through gameplay and is not otherwise purchasable or redeemable using cash or credit or included as part of a paid subscription service; or\n**(ii)**\na purchase of additional levels within the game or an overall expansion of the game.\n**(8) Minor**\nThe term minor means an individual who is under the age of 17.\n**(9) Narcotic drug**\nThe term narcotic drug has the meaning given such term in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ).\n**(10) Online platform**\n**(A) In general**\nThe term online platform means any public-facing website, online service, online application, or mobile application that predominantly provides a community forum for user-generated content, such as sharing videos, images, games, audio files, or other content, including a social media service, social network, or virtual reality environment.\n**(B) Incidental chat functions**\nA website, online service, online application, or mobile application is not an online platform solely on the basis that it includes a chat, comment, or other interactive function that is incidental to its predominant purpose.\n**(11) Online video game**\nThe term online video game means a video game, including an educational video game, that connects to the internet and that allows a user to\u2014\n**(A)**\ncreate and upload content other than content that is incidental to gameplay, such as character or level designs created by the user, preselected phrases, or short interactions with other users;\n**(B)**\nengage in microtransactions within the game; or\n**(C)**\ncommunicate with other users.\n**(12) Parent**\nThe term parent includes a legal guardian.\n**(13) Personal data**\nThe term personal data has the same meaning as the term personal information as defined in section 1302 of the Children\u2019s Online Privacy Protection Act ( 15 U.S.C. 6501 ).\n**(14) Personalized design feature**\nThe term personalized design feature means a fully or partially automated system, including a recommendation system, that is based on the collection of personal data of users and that encourages or increases the frequency, time spent, or activity of minors on the covered platform.\n**(15) Personalized recommendation system**\nThe term personalized recommendation system means a fully or partially automated system used to suggest, promote, or rank content, including other users, hashtags, or posts, based on the personal data of users. A recommendation system that suggests, promotes, or ranks content based solely on the user\u2019s language, city or town, or age shall not be considered a personalized recommendation system.\n**(16) Sexual exploitation and abuse**\nThe term sexual exploitation and abuse means any of the following:\n**(A)**\nCoercion and enticement, as described in section 2422 of title 18, United States Code.\n**(B)**\nChild sexual abuse material, as described in sections 2251, 2252, 2252A, and 2260 of title 18, United States Code.\n**(C)**\nTrafficking for the production of images, as described in section 2251A of title 18, United States Code.\n**(D)**\nSex trafficking of children, as described in section 1591 of title 18, United States Code.\n**(17) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(18) User**\nThe term user means, with respect to a covered platform, an individual who registers an account or creates a profile on the covered platform.\n#### 102. Duty of care\n##### (a) Prevention of harm to minors\nA covered platform shall exercise reasonable care in the creation and implementation of any design feature to prevent and mitigate the following harms to minors where a reasonable and prudent person would agree that such harms were reasonably foreseeable by the covered platform and would agree that the design feature is a contributing factor to such harms:\n**(1)**\nEating disorders, substance use disorders, and suicidal behaviors.\n**(2)**\nDepressive disorders and anxiety disorders when such conditions have objectively verifiable and clinically diagnosable symptoms and are related to compulsive usage.\n**(3)**\nPatterns of use that indicate compulsive usage.\n**(4)**\nPhysical violence or online harassment activity that is so severe, pervasive, or objectively offensive that it impacts a major life activity of a minor.\n**(5)**\nSexual exploitation and abuse of minors.\n**(6)**\nDistribution, sale, or use of narcotic drugs, tobacco products, cannabis products, gambling, or alcohol.\n**(7)**\nFinancial harms caused by unfair or deceptive acts or practices (as defined in section 5(a)(4) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(4) )).\n##### (b) Rules of construction\n**(1)**\nNothing in subsection (a) shall be construed to require a covered platform to prevent or preclude any minor from\u2014\n**(A)**\ndeliberately and independently searching for, or specifically requesting, content; or\n**(B)**\naccessing resources and information regarding the prevention or mitigation of the harms described in subsection (a).\n**(2)**\nNothing in this section shall be construed to allow a government entity to enforce subsection (a) based upon the viewpoint of users expressed by or through any speech, expression, or information protected by the First Amendment to the Constitution of the United States.\n#### 103. Safeguards for minors\n##### (a) Safeguards for minors\n**(1) Safeguards**\nA covered platform shall provide a user or visitor that the covered platform knows is a minor with readily accessible and easy-to-use safeguards to, as applicable\u2014\n**(A)**\nlimit the ability of other users or visitors to communicate with the minor;\n**(B)**\nprevent other users or visitors, whether registered or not, from viewing the minor\u2019s personal data collected by or shared on the covered platform, in particular restricting public access to personal data;\n**(C)**\nlimit by default design features that encourage or increase the frequency, time spent, or activity of minors on the covered platform, such as infinite scrolling, auto playing, rewards for time spent on the platform, notifications, and other design features that result in compulsive usage of the covered platform by the minor;\n**(D)**\ncontrol personalized recommendation systems, including the ability for a minor to have\u2014\n**(i)**\na prominently displayed option to opt out of such personalized recommendation systems, while still allowing the display of content based on a chronological format; and\n**(ii)**\na prominently displayed option to limit types or categories of recommendations from such systems; and\n**(E)**\nrestrict the sharing of the geolocation of the minor and provide notice regarding the tracking of the minor\u2019s geolocation.\n**(2) Option**\nA covered platform shall provide a user that the covered platform knows is a minor with a readily accessible and easy-to-use option to limit the amount of time spent by the minor on the covered platform.\n**(3) Default safeguard settings for minors**\nA covered platform shall provide that, in the case of a user or visitor that the platform knows is a minor, the default setting for any safeguard described under paragraph (1) shall be the option available on the platform that provides the most protective level of control that is offered by the platform over privacy and safety for that user or visitor, unless otherwise enabled by the parent of the minor.\n##### (b) Parental tools\n**(1) Tools**\nA covered platform shall provide readily accessible and easy-to-use parental tools for parents to support a user that the platform knows is a minor with respect to the use of the platform by that user.\n**(2) Requirements**\nThe parental tools provided by a covered platform under paragraph (1) shall include\u2014\n**(A)**\nthe ability to manage a minor\u2019s privacy and account settings, including the safeguards and options established under subsection (a), in a manner that allows parents to\u2014\n**(i)**\nview the privacy and account settings; and\n**(ii)**\nin the case of a user that the platform knows is a child, change and control the privacy and account settings;\n**(B)**\nthe ability to restrict purchases and financial transactions by the minor, where applicable; and\n**(C)**\nthe ability to view metrics of total time spent on the covered platform and restrict time spent on the covered platform by the minor.\n**(3) Notice to minors**\nA covered platform shall provide clear and conspicuous notice to a user when the tools described in this subsection are in effect and what settings or controls have been applied.\n**(4) Default tools**\nA covered platform shall provide that, in the case of a user that the platform knows is a child, the tools required under paragraph (1) shall be enabled by default.\n**(5) Application to existing accounts**\nIf, prior to the effective date of this subsection, a covered platform provided a parent of a user that the platform knows is a child with notice and the ability to enable the parental tools described under this subsection in a manner that would otherwise comply with this subsection, and the parent opted out of enabling such tools, the covered platform is not required to enable such tools with respect to such user by default when this subsection takes effect.\n##### (c) Reporting mechanism\n**(1) Reporting tools**\nA covered platform shall provide\u2014\n**(A)**\na readily accessible and easy-to-use means for users and visitors to submit reports to the covered platform of harms to a minor on the covered platform;\n**(B)**\nan electronic point of contact specific to matters involving harms to a minor; and\n**(C)**\nconfirmation of the receipt of such a report and, within the applicable time period described in paragraph (2), a substantive response to the individual that submitted the report.\n**(2) Timing**\nA covered platform shall establish an internal process to receive and substantively respond to such reports in a reasonable and timely manner, but in no case later than\u2014\n**(A)**\n10 days after the receipt of a report, if, for the most recent calendar year, the platform averaged more than 10,000,000 active users on a monthly basis in the United States;\n**(B)**\n21 days after the receipt of a report, if, for the most recent calendar year, the platform averaged less than 10,000,000 active users on a monthly basis in the United States; and\n**(C)**\nnotwithstanding subparagraphs (A) and (B), if the report involves an imminent threat to the safety of a minor, as promptly as needed to address the reported threat to safety.\n##### (d) Advertising of illegal products\nA covered platform shall not facilitate the advertising of narcotic drugs, cannabis products, tobacco products, gambling, or alcohol to an individual that the covered platform knows is a minor.\n##### (e) Rules of application\n**(1) Accessibility**\nWith respect to safeguards and parental tools described under subsections (a) and (b), a covered platform shall provide\u2014\n**(A)**\ninformation and control options in a clear and conspicuous manner that takes into consideration the differing ages, capacities, and developmental needs of the minors most likely to access the covered platform and does not encourage minors or parents to weaken or disable safeguards or parental tools;\n**(B)**\nreadily accessible and easy-to-use controls to enable or disable safeguards or parental tools, as appropriate; and\n**(C)**\ninformation and control options in the same language, form, and manner as the covered platform provides the product or service used by minors and their parents.\n**(2) Dark patterns prohibition**\nIt shall be unlawful for any covered platform to design, embed, modify, or manipulate a user interface of a covered platform with the purpose or substantial effect of obscuring, subverting or impairing user autonomy, decision-making, or choice with respect to safeguards or parental tools required under this section.\n**(3) Timing considerations**\n**(A) No interruption to gameplay**\nSubsections (a)(1)(C) and (b)(3) shall not require an online video game to interrupt the natural sequence of gameplay, such as progressing through game levels or finishing a competition.\n**(B) Application of changes to offline devices or accounts**\nIf a user\u2019s device or user account does not have access to the internet at the time of a change to parental tools, a covered platform shall apply changes the next time the device or user is connected to the internet.\n##### (f) Device or console controls\n**(1) In general**\nNothing in this section shall be construed to prohibit a covered platform from integrating its products or service with, or duplicate controls or tools provided by, third-party systems, including operating systems or gaming consoles, to meet the requirements imposed under subsections (a) and (b) relating to safeguards for minors and parental tools, provided that\u2014\n**(A)**\nthe controls or tools meet such requirements; and\n**(B)**\nthe minor or parent is provided sufficient notice of the integration and use of the parental tools.\n**(2) Preservation of protections**\nIn the event of a conflict between the controls or tools of a third-party system, including operating systems or gaming consoles, and a covered platform, the covered platform is not required to override the controls or tools of a third-party system if it would undermine the protections for minors from the safeguards or parental tools imposed under subsections (a) and (b).\n##### (g) Exception\nA covered platform shall provide the safeguards and parental tools described in subsections (a) and (b) to an educational agency or institution (as defined in section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g(a)(3) )), rather than to the user or visitor, when the covered platform is acting on behalf of the educational agency or institution subject to a written contract that complies with the requirements of the Children\u2019s Online Privacy Protection Act ( 15 U.S.C. 6501 et seq. ) and the Family Educational Rights and Privacy Act of 1974 ( 20 U.S.C. 1232g ).\n##### (h) Rules of construction\nNothing in this section shall be construed to\u2014\n**(1)**\nprevent a covered platform from taking reasonable measures to\u2014\n**(A)**\nblock, detect, or prevent the distribution of unlawful, obscene, or other harmful material to minors as described in section 102(a); or\n**(B)**\nblock or filter spam, prevent criminal activity, or protect the security of a platform or service;\n**(2)**\nrequire the disclosure of the browsing behavior, search history, messages, contact list, or other content or metadata of the communications of a minor;\n**(3)**\nprevent a covered platform from using a personalized recommendation system to display content to a minor if the system only uses information on\u2014\n**(A)**\nthe language spoken by the minor;\n**(B)**\nthe city the minor is located in; or\n**(C)**\nthe minor\u2019s age;\n**(4)**\nprevent an online video game from disclosing a username or other user identification for the purpose of competitive gameplay or to allow for the reporting of users;\n**(5)**\nprevent a covered platform from contracting or entering into an agreement with a third-party entity, whose primary or exclusive function is to provide the safeguards or parental tools required under subsections (a) and (b) or to offer similar or stronger protective capabilities for minors, to assist with meeting the requirements imposed under subsections (a) and (b); or\n**(6)**\nprevent a parent or user from authorizing a third-party entity described in subparagraph (5) to implement such safeguards or parental tools or provide similar or stronger protective capabilities for minors, at the choice of the parent or user.\n#### 104. Disclosure\n##### (a) Notice\n**(1) Registration or purchase**\nPrior to registration or purchase of a covered platform by an individual that the platform knows is a minor, the platform shall provide clear, conspicuous, and easy-to-understand\u2014\n**(A)**\nnotice of the policies and practices of the covered platform with respect to safeguards for minors;\n**(B)**\ninformation about how to access the safeguards and parental tools required under section 103; and\n**(C)**\nnotice about how to access the information on personalized recommendation systems required under subsection (b).\n**(2) Notification**\n**(A) Notice and acknowledgment**\nIn the case of an individual that a covered platform knows is a child, the platform shall provide information about the parental tools and safeguards required under section 103 to a parent of the child and obtain verifiable consent (as defined in section 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 )).\n**(B) Reasonable effort**\nA covered platform shall be deemed to have satisfied the requirement described in subparagraph (A) if the covered platform is in compliance with the requirements of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. ) to use reasonable efforts (taking into consideration available technology) to provide a parent with the information described in subparagraph (A) and to obtain verifiable consent as required.\n**(3) Consolidated notices**\nFor purposes of this title, a covered platform may consolidate the process for providing information under this subsection and obtaining verifiable consent or the consent of the minor involved (as applicable) as required under this subsection with the obligations of the covered platform to provide relevant notice and obtain verifiable consent under the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. ).\n**(4) Guidance**\nThe Federal Trade Commission may issue guidance to assist covered platforms in complying with the specific notice requirements of this subsection.\n##### (b) Personalized recommendation system\nA covered platform that operates a personalized recommendation system shall set out in its terms and conditions, in a clear, conspicuous, and easy-to-understand manner\u2014\n**(1)**\nan overview of how each personalized recommendation system is used by the covered platform to provide information to minors, including how such systems use the personal data of minors; and\n**(2)**\ninformation about options for minors or their parents to opt out of or control the personalized recommendation system (as applicable).\n##### (c) Advertising and marketing information and labels\n**(1) Information and labels**\nA covered platform shall provide clear, conspicuous, and easy-to-understand labels and information, which can be provided through a link to another web page or disclosure, to minors on advertisements regarding\u2014\n**(A)**\nthe name of the product, service, or brand and the subject matter of an advertisement; and\n**(B)**\nwhether particular media displayed to the minor is an advertisement or marketing material, including disclosure of endorsements of products, services, or brands made for commercial consideration by other users of the platform.\n**(2) Guidance**\nThe Federal Trade Commission may issue guidance to assist covered platforms in complying with the requirements of this subsection, including guidance about the minimum level of information and labels for the disclosures required under paragraph (1).\n##### (d) Resources for parents and minors\nA covered platform shall provide to minors and parents clear, conspicuous, easy-to-understand, and comprehensive information in a prominent location, which may include a link to a web page, regarding\u2014\n**(1)**\nthe policies and practices of the covered platform with respect to safeguards for minors; and\n**(2)**\nhow to access the safeguards and parental tools required under section 103.\n##### (e) Resources in additional languages\nA covered platform shall ensure, to the extent practicable, that the disclosures required by this section are made available in the same language, form, and manner as the covered platform provides any product or service used by minors and their parents.\n#### 105. Transparency\n##### (a) In general\nSubject to subsection (b), not less frequently than once a year, a covered platform shall issue a public report that addresses the matters in subsection (c) based on an independent, third-party audit of the covered platform with a reasonable level of assurance.\n##### (b) Scope of application\nThe requirements of this section shall apply to a covered platform if\u2014\n**(1)**\nfor the most recent calendar year, the platform averaged more than 10,000,000 active users on a monthly basis in the United States; and\n**(2)**\nthe platform predominantly provides a community forum for user-generated content and discussion, including sharing videos, images, games, audio files, discussion in a virtual setting, or other content, such as acting as a social media platform, virtual reality environment, or a social network service.\n##### (c) Content\n**(1) Transparency**\nThe public reports required of a covered platform under this section shall include\u2014\n**(A)**\nan assessment of the extent to which the platform is likely to be accessed by minors;\n**(B)**\na description of the commercial interests of the covered platform being used by minors;\n**(C)**\nan accounting, based on the data held by the covered platform, of\u2014\n**(i)**\nthe number of users using the covered platform that the platform knows to be minors in the United States;\n**(ii)**\nthe median and mean amounts of time spent on the platform by users known to be minors in the United States who have accessed the platform during the reporting year on a daily, weekly, and monthly basis; and\n**(iii)**\nthe amount of content being accessed by users that the platform knows to be minors in the United States that is in English, and the top 5 non-English languages used by users accessing the platform in the United States;\n**(D)**\nan accounting of total reports received through the reporting mechanism described in section 103, disaggregated by language, including English and the top 5 non-English languages used by users accessing the platform from the United States (as identified under subparagraph (C)(iii)); and\n**(E)**\nan assessment of the safeguards and parental tools under section 103, representations regarding the use of the personal data of minors, and other matters regarding compliance with this title.\n**(2) Evaluation**\nThe public reports required under this section shall include\u2014\n**(A)**\nan assessment based on aggregate data on the exercise of safeguards and parental tools described in section 103, and other competent and reliable empirical evidence;\n**(B)**\na description of whether and how the covered platform uses design features that increase, sustain, or extend the use of a product or service by a minor;\n**(C)**\na description of whether, how, and for what purpose the platform collects or processes categories of personal data, including how personal data is used to operate personalized recommendation systems related to minors;\n**(D)**\nan evaluation of the efficacy of safeguards for minors and parental tools under section 103, and any issues in delivering such safeguards and parental tools; and\n**(E)**\nan assessment of differences, with respect to the matters described in subparagraphs (A) through (D), across different English and non-English languages and efficacy of safeguards in those languages.\n**(3) Mitigation**\nThe public reports required of a covered platform under this section shall include, for English and the top 5 non-English languages used by users accessing the platform from the United States (as identified under paragraph (2)(C)(iii))\u2014\n**(A)**\na description of the safeguards and parental tools available to minors and parents on the covered platform;\n**(B)**\na description of the prevention and mitigation measures a covered platform may take, if any, in response to the assessments conducted under paragraph (2), including steps take to provide the most protective level of control over safety by default;\n**(C)**\na description of the processes used for the creation and implementation of any design feature that will be used by minors;\n**(D)**\na description and assessment of handling reports under the requirement of section 103(c), including the rate of response, timeliness, and substantiveness of responses; and\n**(E)**\nthe status of implementing prevention and mitigation measures identified in prior assessments.\n##### (d) Reasonable inspection\nIn conducting an inspection of the reasonably foreseeable risk of harm to minors under this section, an independent, third-party auditor shall\u2014\n**(1)**\ntake into consideration the function of personalized recommendation systems;\n**(2)**\nconsult parents and youth experts, including youth and families with relevant past or current experience, public health and mental health nonprofit organizations, health and development organizations, and civil society with respect to the prevention of harms to minors;\n**(3)**\nconduct research based on experiences of minors that use the covered platform, including reports under section 103(c) and information provided by law enforcement;\n**(4)**\ntake account of research, including research regarding design features, marketing, or product integrity, industry best practices, or outside research;\n**(5)**\ntake into consideration indicia or inferences of age of users, in addition to any self-declared information about the age of users; and\n**(6)**\ntake into consideration differences in risk of reasonably foreseeable harms and effectiveness of safeguards across English and non-English languages.\n##### (e) Cooperation with independent, third-Party audit\nTo facilitate the report required by subsection (c), a covered platform shall\u2014\n**(1)**\nprovide or otherwise make available to the independent third-party conducting the audit all information and material in its possession, custody, or control that is relevant to the audit;\n**(2)**\nprovide or otherwise make available to the independent third-party conducting the audit access to all network, systems, and assets relevant to the audit; and\n**(3)**\ndisclose all relevant facts to the independent third-party conducting the audit, and not misrepresent in any manner, expressly or by implication, any relevant fact.\n##### (f) Privacy safeguards\n**(1) In general**\nIn issuing the public reports required under this section, a covered platform shall take steps to safeguard the privacy of its users, including ensuring that data is presented in a de-identified, aggregated format such that it is not reasonably linkable to any user.\n**(2) Rule of construction**\nThis section shall not be construed to require the disclosure of information that will lead to material vulnerabilities for the privacy of users or the security of a covered platform\u2019s service or create a significant risk of the violation of Federal or State law.\n**(3) Definition of de-identified**\nAs used in this subsection, the term de-identified means data that does not identify and is not linked or reasonably linkable to a device that is linked or reasonably linkable to an individual, regardless of whether the information is aggregated.\n##### (g) Location\nThe public reports required under this section should be posted by a covered platform on an easy to find location on a publicly available website.\n#### 106. Market research\n##### (a) Prohibition of research on children\nA covered platform shall not, in the case of a user or visitor that the covered platform knows is a child, conduct market or product-focused research on such child.\n##### (b) Market research on minors\nA covered platform may not, in the case of a user or visitor that the online platform knows is a minor, conduct market or product-focused research on such minor, unless the covered platform obtains verifiable parental consent (as defined in section 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 )) prior to conducting such research on such minor.\n#### 107. Age verification study and report\n##### (a) Study\nThe Secretary of Commerce, in coordination with the Federal Communications Commission and the Federal Trade Commission, shall conduct a study evaluating the most technologically feasible methods and options for developing systems to verify age at the device or operating system level.\n##### (b) Contents\nSuch study shall consider\u2014\n**(1)**\nthe benefits of creating a device or operating system level age verification system;\n**(2)**\nwhat information may need to be collected to create this type of age verification system;\n**(3)**\nthe accuracy of such systems and their impact or steps to improve accessibility, including for individuals with disabilities;\n**(4)**\nhow such a system or systems could verify age while mitigating risks to user privacy and data security and safeguarding minors\u2019 personal data, emphasizing minimizing the amount of data collected and processed by covered platforms and age verification providers for such a system;\n**(5)**\nthe technical feasibility, including the need for potential hardware and software changes, including for devices currently in commerce and owned by consumers; and\n**(6)**\nthe impact of different age verification systems on competition, particularly the risk of different age verification systems creating barriers to entry for small companies.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the agencies described in subsection (a) shall submit a report containing the results of the study conducted under such subsection to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives.\n#### 108. Guidance\n##### (a) In general\nNot later than 18 months after the date of enactment of this Act, the Federal Trade Commission shall issue guidance to\u2014\n**(1)**\nprovide information and examples for covered platforms and auditors regarding the following, with consideration given to differences across English and non-English languages\u2014\n**(A)**\nidentifying design features that encourage or increase the frequency, time spent, or activity of minors on the covered platform;\n**(B)**\nsafeguarding minors against the possible misuse of parental tools;\n**(C)**\nbest practices in providing minors and parents the most protective level of control over privacy and safety;\n**(D)**\nusing indicia or inferences of age of users for assessing use of the covered platform by minors;\n**(E)**\nmethods for evaluating the efficacy of safeguards set forth in this title; and\n**(F)**\nproviding additional parental tool options that allow parents to address the harms described in section 102(a); and\n**(2)**\noutline conduct that does not have the purpose or substantial effect of subverting or impairing user autonomy, decision-making, or choice, or of causing, increasing, or encouraging compulsive usage for a minor, such as\u2014\n**(A)**\nde minimis user interface changes derived from testing consumer preferences, including different styles, layouts, or text, where such changes are not done with the purpose of weakening or disabling safeguards or parental tools;\n**(B)**\nalgorithms or data outputs outside the control of a covered platform; and\n**(C)**\nestablishing default settings that provide enhanced privacy protection to users or otherwise enhance their autonomy and decision-making ability.\n##### (b) Guidance on knowledge standard\nNot later than 18 months after the date of enactment of this Act, the Federal Trade Commission shall issue guidance to provide information, including best practices and examples, for covered platforms to understand how the Commission would determine whether a covered platform had knowledge fairly implied on the basis of objective circumstances for purposes of this title.\n##### (c) Limitation on Federal Trade Commission guidance\n**(1) Effect of guidance**\nNo guidance issued by the Federal Trade Commission with respect to this title shall\u2014\n**(A)**\nconfer any rights on any person, State, or locality; or\n**(B)**\noperate to bind the Federal Trade Commission or any court, person, State, or locality to the approach recommended in such guidance.\n**(2) Use in enforcement actions**\nIn any enforcement action brought pursuant to this title, the Federal Trade Commission or a State attorney general, as applicable\u2014\n**(A)**\nshall allege a violation of a provision of this title; and\n**(B)**\nmay not base such enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with guidance issued by the Federal Trade Commission with respect to this title, unless the practices are alleged to violate a provision of this title.\nFor purposes of\n                            enforcing this title, State attorneys general shall take into account\n                            any guidance issued by the Commission under subsection\n (b).\n#### 109. Enforcement\n##### (a) Enforcement by Federal Trade Commission\n**(1) Unfair and deceptive acts or practices**\nA violation of this title shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Federal Trade Commission (referred to in this section as the Commission ) shall enforce this title in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this title.\n**(B) Privileges and immunities**\nAny person that violates this title shall be subject to the penalties, and entitled to the privileges and immunities, provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this title shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Enforcement by State attorneys general\n**(1) In general**\n**(A) Civil actions**\nIn any case in which the attorney general of a State has reason to believe that a covered platform has violated or is violating section 103, 104, or 105, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in a district court of the United States or a State court of appropriate jurisdiction to\u2014\n**(i)**\nenjoin any practice that violates section 103, 104, or 105;\n**(ii)**\nenforce compliance with section 103, 104, or 105;\n**(iii)**\non behalf of residents of the State, obtain damages, restitution, or other compensation, each of which shall be distributed in accordance with State law; or\n**(iv)**\nobtain such other relief as the court may consider to be appropriate.\n**(B) Notice**\n**(i) In general**\nBefore filing an action under subparagraph (A), the attorney general of the State involved shall provide to the Commission\u2014\n**(I)**\nwritten notice of that action; and\n**(II)**\na copy of the complaint for that action.\n**(ii) Exemption**\n**(I) In general**\nClause (i) shall not apply with respect to the filing of an action by an attorney general of a State under this paragraph if the attorney general of the State determines that it is not feasible to provide the notice described in that clause before the filing of the action.\n**(II) Notification**\nIn an action described in subclause (I), the attorney general of a State shall provide notice and a copy of the complaint to the Commission at the same time as the attorney general files the action.\n**(2) Intervention**\n**(A) In general**\nOn receiving notice under paragraph (1)(B), the Commission shall have the right to intervene in the action that is the subject of the notice.\n**(B) Effect of intervention**\nIf the Commission intervenes in an action under paragraph (1), it shall have the right\u2014\n**(i)**\nto remove the action to the appropriate United States district court;\n**(ii)**\nto be heard with respect to any matter that arises in that action; and\n**(iii)**\nto file a petition for appeal.\n**(3) Construction**\nFor purposes of bringing any civil action under paragraph (1), nothing in this title shall be construed to prevent an attorney general of a State from exercising the powers conferred on the attorney general by the laws of that State to\u2014\n**(A)**\nconduct investigations;\n**(B)**\nadminister oaths or affirmations; or\n**(C)**\ncompel the attendance of witnesses or the production of documentary and other evidence.\n**(4) Actions by the commission**\nIn any case in which an action is instituted by or on behalf of the Commission for violation of this title, no State may, during the pendency of that action, institute a separate action under paragraph (1) against any defendant named in the complaint in the action instituted by or on behalf of the Commission for that violation.\n**(5) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\na State court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1) in a district court of the United States, process may be served wherever defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n**(6) Limitation**\nA violation of section 102 shall not form the basis of liability in any action brought by the attorney general of a State under a State law.\n#### 110. Kids online safety council\n##### (a) Establishment\nThere is established a Kids Online Safety Council (in this section referred to as the Council ).\n##### (b) Duties\nThe duties of the Council shall be to provide reports to Congress with recommendations and advice on matters related to the safety of minors online. The matters to be addressed by the Council shall include\u2014\n**(1)**\nidentifying emerging or current risks of harms to minors associated with online platforms;\n**(2)**\nrecommending measures and methods for assessing, preventing, and mitigating harms to minors online;\n**(3)**\nrecommending methods and themes for conducting research regarding online harms to minors, including in English and non-English languages; and\n**(4)**\nrecommending best practices and clear, consensus-based technical standards for transparency reports and audits, as required under this title, including methods, criteria, and scope to promote overall accountability.\n##### (c) Number and appointment of members\nThe Council shall be comprised of 11 members, of whom\u2014\n**(1)**\n3 members shall be appointed by the President, including\u2014\n**(A)**\nthe Secretary of Commerce or a designee of the Secretary; and\n**(B)**\nthe Secretary of Health and Human Services or a designee of the Secretary;\n**(2)**\n2 members shall be appointed by the Speaker of the House of Representatives;\n**(3)**\n2 members shall be appointed by the Minority Leader of the House of Representatives;\n**(4)**\n2 members shall be appointed by the Majority Leader of the Senate; and\n**(5)**\n2 members shall be appointed by the Minority Leader of the Senate.\n##### (d) Timing of appointments\nEach of the appointments under subsection (c) shall be made not later than 180 days after the date of the enactment of this Act.\n##### (e) Terms; vacancies\nEach member of the Council shall be appointed for the life of the Council, and a vacancy in the Council shall be filled in the manner in which the original appointment was made.\n##### (f) Chairperson; vice chairperson\nThe Council, once it has been fully appointed, shall select its own Chair and Vice Chair.\n##### (g) Participation\nThe Council shall consist of 1 member from each of the following:\n**(1)**\nacademic experts with specific expertise in the prevention of online harms to minors;\n**(2)**\nresearchers with specific expertise in social media studies;\n**(3)**\nparents with demonstrated experience in child online safety;\n**(4)**\nyouth representatives with demonstrated experience in child online safety;\n**(5)**\neducators with demonstrated experience in child online safety;\n**(6)**\nrepresentatives of online platforms;\n**(7)**\nrepresentatives of online video games;\n**(8)**\nState attorneys general or their designees acting in State or local government; and\n**(9)**\nrepresentatives of communities of socially disadvantaged individuals (as defined in section 8 of the Small Business Act ( 15 U.S.C. 637 )).\n##### (h) Reports\n**(1) Interim report**\nNot later than 1 year after the date of the initial meeting of the Council, the Council shall submit to Congress an interim report that includes a detailed summary of the work of the Council and any preliminary findings of the Council.\n**(2) Final report**\nNot later than 3 years after the date of the initial meeting of the Council, the Council shall submit to Congress a final report that includes\u2014\n**(A)**\na detailed statement of the findings and conclusions of the Council;\n**(B)**\ndissenting opinions of any member of the Council who does not support the findings and conclusions referred to in subparagraph (A); and\n**(C)**\nany recommendations for legislative and administrative actions to address online safety for children and prevent harms to minors.\n##### (i) Termination\nThe Council shall terminate not later than 30 days after the submission of the final report required under subsection (h)(2).\n##### (j) Non-Applicability of FACA\nThe Kids Online Safety Council shall not be subject to chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ).\n#### 111. Effective date\nExcept as otherwise provided in this title, this title shall take effect on the date that is 18 months after the date of enactment of this Act.\n#### 112. Rules of construction and other matters\n##### (a) Relationship to other laws\nNothing in this title shall be construed to\u2014\n**(1)**\npreempt section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g , commonly known as the Family Educational Rights and Privacy Act of 1974 ) or other Federal or State laws governing student privacy;\n**(2)**\npreempt the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. ) or any rule or regulation promulgated under such Act;\n**(3)**\nauthorize any action that would conflict with section 18(h) of the Federal Trade Commission Act ( 15 U.S.C. 57a(h) ); or\n**(4)**\nexpand, limit the scope, or alter the meaning of section 230 of the Communications Act of 1934 (commonly known as section 230 of the Communications Decency Act of 1996 ) ( 47 U.S.C. 230 ).\n##### (b) Determination of fairly implied on the basis of objective circumstances\nFor purposes of enforcing this title, in making a determination as to whether covered platform has knowledge fairly implied on the basis of objective circumstances that a specific user is a minor, the Federal Trade Commission or a State attorney general shall rely on competent and reliable evidence, taking into account the totality of the circumstances, including whether a reasonable and prudent person under the circumstances would have known that the user is a minor.\n##### (c) Protections for privacy\nNothing in this title, including a determination described in subsection (b), shall be construed to require\u2014\n**(1)**\nthe affirmative collection of any personal data with respect to the age of users that a covered platform is not already collecting in the normal course of business; or\n**(2)**\na covered platform to implement an age gating or age verification functionality.\n##### (d) Compliance\nNothing in this title shall be construed to restrict a covered platform\u2019s ability to\u2014\n**(1)**\ncooperate with law enforcement agencies regarding activity that the covered platform reasonably and in good faith believes may violate Federal, State, or local laws, rules, or regulations;\n**(2)**\ncomply with a lawful civil, criminal, or regulatory inquiry, subpoena, or summons by Federal, State, local, or other government authorities;\n**(3)**\ninvestigate, establish, exercise, respond to, or defend against legal claims;\n**(4)**\nprevent, detect, protect against, or respond to any security incident, identity theft, fraud, harassment, malicious or deceptive activity, or any illegal activities; or\n**(5)**\ninvestigate or report those responsible for any action described in paragraph (4).\n##### (e) Application to video streaming services\nA video streaming service shall be deemed to be in compliance with this title if it predominantly consists of news, sports, entertainment, or other video programming content that is preselected by the provider and not user-generated, and\u2014\n**(1)**\nany chat, comment, or interactive functionality is provided incidental to, directly related to, or dependent on provision of such content; and\n**(2)**\nif such video streaming service requires account owner registration and is not predominantly news or sports, the service includes the capability\u2014\n**(A)**\nto limit a minor\u2019s access to the service, which may utilize a system of age-rating;\n**(B)**\nto limit the automatic playing of on-demand content selected by a personalized recommendation system for an individual that the service knows is a minor;\n**(C)**\nfor a parent to manage a minor\u2019s privacy and account settings, and restrict purchases and financial transactions by a minor, where applicable;\n**(D)**\nto provide an electronic point of contact specific to matters described in this paragraph;\n**(E)**\nto offer a clear, conspicuous, and easy-to-understand notice of its policies and practices with respect to the capabilities described in this paragraph; and\n**(F)**\nwhen providing on-demand content, to employ measures that safeguard against serving advertising for narcotic drugs, cannabis products, tobacco products, gambling, or alcohol directly to the account or profile of an individual that the service knows is a minor.\nII\nFilter Bubble Transparency\n#### 201. Definitions\nIn this title:\n**(1) Algorithmic ranking system**\nThe term algorithmic ranking system means a computational process, including one derived from algorithmic decision-making, machine learning, statistical analysis, or other data processing or artificial intelligence techniques, used to determine the selection, order, relative prioritization, or relative prominence of content from a set of information that is provided to a user on an online platform, including the ranking of search results, the provision of content recommendations, the display of social media posts, or any other method of automated content selection.\n**(2) Approximate geolocation information**\nThe term approximate geolocation information means information that identifies the location of an individual, but with a precision of less than 5 miles.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Connected device**\nThe term connected device means an electronic device that\u2014\n**(A)**\nis capable of connecting to the internet, either directly or indirectly through a network, to communicate information at the direction of an individual;\n**(B)**\nhas computer processing capabilities for collecting, sending, receiving, or analyzing data; and\n**(C)**\nis primarily designed for or marketed to consumers.\n**(5) Input-transparent algorithm**\n**(A) In general**\nThe term input-transparent algorithm means an algorithmic ranking system that does not use the user-specific data of a user to determine the selection, order, relative prioritization, or relative prominence of information that is furnished to such user on an online platform, unless the user-specific data is expressly provided to the platform by the user for such purpose.\n**(B) Data expressly provided to the platform**\nFor purposes of subparagraph (A), user-specific data that is provided by a user for the express purpose of determining the selection, order, relative prioritization, or relative prominence of information that is furnished to such user on an online platform\u2014\n**(i)**\nincludes user-supplied search terms, filters, speech patterns (if provided for the purpose of enabling the platform to accept spoken input or selecting the language in which the user interacts with the platform), saved preferences, the resumption of a previous search, and the current precise geolocation information that is supplied by the user;\n**(ii)**\nincludes the user\u2019s current approximate geolocation information;\n**(iii)**\nincludes data submitted to the platform by the user that expresses the user\u2019s desire to receive particular information, such as the social media profiles the user follows, the video channels the user subscribes to, or other content or sources of content on the platform the user has selected;\n**(iv)**\ndoes not include the history of the connected device of the user, including the history of web searches and browsing, previous geographical locations, physical activity, device interaction, and financial transactions of the user; and\n**(v)**\ndoes not include inferences about the user or the connected device of the user, without regard to whether such inferences are based on data described in clause (i) or (iii).\n**(6) Online platform**\n**(A) In general**\nSubject to subparagraph (B), the term online platform means any public-facing website, online service, online application, or mobile application that predominantly provides a community forum for user-generated content, such as sharing videos, images, games, audio files, or other content, including a social media service, social network, or virtual reality environment.\n**(B) Scope**\n**(i) Incidental chat functions**\nA website, online service, online application, or mobile application is not an online platform solely on the basis that it includes a chat, comment, or other interactive function that is incidental to its predominant purpose.\n**(ii) Review sites**\nA website, online service, online application, or mobile application that has the predominant purpose of providing travel reviews is not an online platform.\n**(7) Opaque algorithm**\nThe term opaque algorithm \u2014\n**(A)**\nmeans an algorithmic ranking system that determines the selection, order, relative prioritization, or relative prominence of information that is furnished to such user on an online platform based, in whole or part, on user-specific data that was not expressly provided by the user to the platform for such purpose; and\n**(B)**\ndoes not include an algorithmic ranking system used by an online platform if\u2014\n**(i)**\nthe only user-specific data (including inferences about the user) that the system uses is information relating to the age of the user; and\n**(ii)**\nsuch information is only used to restrict the access of a user to content on the basis that the individual is not old enough to access such content.\n**(8) Precise geolocation information**\nThe term precise geolocation information means geolocation information that identifies the location of an individual to within a range of 5 miles or less.\n**(9) User-specific data**\nThe term user-specific data means information relating to an individual or a specific connected device that would not necessarily be true of every individual or device.\n#### 202. Requirement to allow users to see unmanipulated content on internet platforms\n##### (a) In general\nBeginning on the date that is 1 year after the date of enactment of this Act, it shall be unlawful for any person to operate an online platform that uses an opaque algorithm unless the person complies with the requirements of subsection (b).\n##### (b) Opaque algorithm requirements\n**(1) In general**\nThe requirements of this subsection with respect to a person that operates an online platform that uses an opaque algorithm are the following:\n**(A)**\nThe person provides users of the platform with the following notices:\n**(i)**\nNotice that the platform uses an opaque algorithm that uses user-specific data to select the content the user sees. Such notice shall be presented in a clear and conspicuous manner on the platform whenever the user interacts with an opaque algorithm for the first time, and may be a one-time notice that can be dismissed by the user.\n**(ii)**\nNotice, to be included in the terms and conditions of the online platform, in a clear, accessible, and easily comprehensible manner that is to be updated whenever the online platform makes a material change, of\u2014\n**(I)**\nthe most salient features, inputs, and parameters used by the algorithm;\n**(II)**\nhow any user-specific data used by the algorithm is collected or inferred about a user of the platform, and the categories of such data;\n**(III)**\nany options that the online platform makes available for a user of the platform to opt out or exercise options under subparagraph (B), modify the profile of the user or to influence the features, inputs, or parameters used by the algorithm; and\n**(IV)**\nany quantities, such as time spent using a product or specific measures of engagement or social interaction, that the algorithm is designed to optimize, as well as a general description of the relative importance of each quantity for such ranking.\n**(B)**\nThe online platform enables users to easily switch between the opaque algorithm and an input-transparent algorithm in their use of the platform.\n**(2) Rule of construction**\nNothing in this subsection shall be construed to require an online platform to disclose any information, including data or algorithms\u2014\n**(A)**\nrelating to a trade secret or other protected intellectual property;\n**(B)**\nthat is confidential business information; or\n**(C)**\nthat is privileged.\n**(3) Prohibition on differential pricing**\nAn online platform shall not deny, charge different prices or rates for, or condition the provision of a service or product to a user based on the user\u2019s election to use an input-transparent algorithm in their use of the platform, as provided under paragraph (1)(B).\n**(4) Special rule**\nNotwithstanding paragraphs (1) and (2), an online platform shall provide the notice and opt-out described in paragraphs (1) and (2) to the educational agency or institution (as defined in section 444(a)(3) of the General Education Provisions Act ( 20 U.S.C. 1232g(a)(3) ), rather than to the user, when the online platform is acting on behalf of an educational agency or institution (as so defined), subject to a written contract that complies with the requirements of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 1232g(a)(3) ) and section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g ) (commonly known as the Family Educational Rights and Privacy Act of 1974 ).\n##### (c) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section by an operator of an online platform shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of commission**\n**(A) In general**\nThe Federal Trade Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n##### (d) Rule of construction To preserve personalized blocks\nNothing in this section shall be construed to limit or prohibit an online platform\u2019s ability to, at the direction of an individual user or group of users, restrict another user from searching for, finding, accessing, or interacting with such user\u2019s or group\u2019s account, content, data, or online community.\nIII\nRelationship to State laws; severability\n#### 301. Relationship to State laws\nThe provisions of this Act shall preempt any State law, rule, or regulation only to the extent that such State law, rule, or regulation conflicts with a provision of this Act. Nothing in this Act shall be construed to prohibit a State from enacting a law, rule, or regulation that provides greater protection to minors than the protection provided by the provisions of this Act.\n#### 302. Severability\nIf any provision of this Act, or an amendment made by this Act, is determined to be unenforceable or invalid, the remaining provisions of this Act and the amendments made by this Act shall not be affected.",
      "versionDate": "2025-05-14",
      "versionType": "Introduced in Senate"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-28T13:01:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-14",
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
          "measure-id": "id119s1748",
          "measure-number": "1748",
          "measure-type": "s",
          "orig-publish-date": "2025-05-14",
          "originChamber": "SENATE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1748v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-05-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Kids Online Safety Act</strong></p><p>This bill requires covered online platforms, including social media platforms, to implement tools and safeguards to protect users and visitors under the age of 17. <em>Covered platforms</em> are online platforms, video games, messaging applications, or video streaming services used or likely to be used by individuals under the age of 17, with specified exceptions.\u00a0</p><p>The bill generally requires covered platforms to exercise reasonable care in the design and use of features that increase minors\u2019 online activity in order to prevent and mitigate harm to minors (e.g., mental health disorders and severe harassment). \u00a0</p><p>Covered platforms are also required to provide certain safeguards to minors, such as protections for minors\u2019 data; tools for parents of minors, such as access to minors\u2019 privacy settings; and a mechanism for account\u00a0holders and visitors to report harm to minors on the platform.\u00a0</p><p>Covered platforms are prohibited from conducting market or product research on children under the age of 13, and may only conduct such research on those under the age of 17 with parental consent.\u00a0</p><p>The bill provides for enforcement through the Federal Trade Commission and states.\u00a0</p><p>The bill also requires online platforms to meet certain requirements before using algorithms that select, order, or prioritize information presented to users based on user-specific data not provided for that purpose. Specifically, such platforms must (1) provide users with notice of the use of such algorithms, and (2) permit users to switch to an algorithm\u00a0that does not rely on such user-specific data.\u00a0</p>"
        },
        "title": "Kids Online Safety Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1748.xml",
    "summary": {
      "actionDate": "2025-05-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Kids Online Safety Act</strong></p><p>This bill requires covered online platforms, including social media platforms, to implement tools and safeguards to protect users and visitors under the age of 17. <em>Covered platforms</em> are online platforms, video games, messaging applications, or video streaming services used or likely to be used by individuals under the age of 17, with specified exceptions.\u00a0</p><p>The bill generally requires covered platforms to exercise reasonable care in the design and use of features that increase minors\u2019 online activity in order to prevent and mitigate harm to minors (e.g., mental health disorders and severe harassment). \u00a0</p><p>Covered platforms are also required to provide certain safeguards to minors, such as protections for minors\u2019 data; tools for parents of minors, such as access to minors\u2019 privacy settings; and a mechanism for account\u00a0holders and visitors to report harm to minors on the platform.\u00a0</p><p>Covered platforms are prohibited from conducting market or product research on children under the age of 13, and may only conduct such research on those under the age of 17 with parental consent.\u00a0</p><p>The bill provides for enforcement through the Federal Trade Commission and states.\u00a0</p><p>The bill also requires online platforms to meet certain requirements before using algorithms that select, order, or prioritize information presented to users based on user-specific data not provided for that purpose. Specifically, such platforms must (1) provide users with notice of the use of such algorithms, and (2) permit users to switch to an algorithm\u00a0that does not rely on such user-specific data.\u00a0</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119s1748"
    },
    "title": "Kids Online Safety Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Kids Online Safety Act</strong></p><p>This bill requires covered online platforms, including social media platforms, to implement tools and safeguards to protect users and visitors under the age of 17. <em>Covered platforms</em> are online platforms, video games, messaging applications, or video streaming services used or likely to be used by individuals under the age of 17, with specified exceptions.\u00a0</p><p>The bill generally requires covered platforms to exercise reasonable care in the design and use of features that increase minors\u2019 online activity in order to prevent and mitigate harm to minors (e.g., mental health disorders and severe harassment). \u00a0</p><p>Covered platforms are also required to provide certain safeguards to minors, such as protections for minors\u2019 data; tools for parents of minors, such as access to minors\u2019 privacy settings; and a mechanism for account\u00a0holders and visitors to report harm to minors on the platform.\u00a0</p><p>Covered platforms are prohibited from conducting market or product research on children under the age of 13, and may only conduct such research on those under the age of 17 with parental consent.\u00a0</p><p>The bill provides for enforcement through the Federal Trade Commission and states.\u00a0</p><p>The bill also requires online platforms to meet certain requirements before using algorithms that select, order, or prioritize information presented to users based on user-specific data not provided for that purpose. Specifically, such platforms must (1) provide users with notice of the use of such algorithms, and (2) permit users to switch to an algorithm\u00a0that does not rely on such user-specific data.\u00a0</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119s1748"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1748is.xml"
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
      "title": "Kids Online Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kids Online Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-24T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the safety of children on the internet.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T03:33:20Z"
    }
  ]
}
```
