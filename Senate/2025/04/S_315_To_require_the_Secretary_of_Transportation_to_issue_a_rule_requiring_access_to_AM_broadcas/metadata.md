# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/315
- Title: AM Radio for Every Vehicle Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 315
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-10-09T00:06:28Z
- Update date including text: 2025-10-09T00:06:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-03 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-11.
- 2025-04-03 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-11.
- 2025-04-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 39.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-03 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-11.
- 2025-04-03 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-11.
- 2025-04-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 39.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/315",
    "number": "315",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "AM Radio for Every Vehicle Act of 2025",
    "type": "S",
    "updateDate": "2025-10-09T00:06:28Z",
    "updateDateIncludingText": "2025-10-09T00:06:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 39.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-11.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-11.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
            "date": "2025-04-03T17:02:33Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T15:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T21:28:16Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TX"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "WI"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "IN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WY"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CT"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "WA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
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
      "sponsorshipDate": "2025-01-29",
      "state": "DE"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AR"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "ND"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "IA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NE"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "IA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NH"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "HI"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "ND"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WV"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-29",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "MN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "OK"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NM"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WY"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "KS"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "OR"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "KS"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CT"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "RI"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SD"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-29",
      "state": "VT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "FL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NH"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "MN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AK"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "OR"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "IN"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MS"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "ME"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AK"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "OK"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NV"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NV"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AR"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "PA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "RI"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "ID"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "LA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "AL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "FL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s315is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 315\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Markey (for himself, Mr. Cruz , Ms. Baldwin , Mr. Banks , Mr. Barrasso , Mrs. Blackburn , Mr. Blumenthal , Mrs. Britt , Mr. Budd , Ms. Cantwell , Mrs. Capito , Mr. Coons , Mr. Cotton , Mr. Cramer , Mr. Daines , Ms. Ernst , Mrs. Fischer , Mr. Grassley , Ms. Hassan , Mr. Hawley , Ms. Hirono , Mr. Hoeven , Mr. Justice , Mr. King , Ms. Klobuchar , Mr. Lankford , Mr. Luj\u00e1n , Ms. Lummis , Mr. Marshall , Mr. Merkley , Mr. Moran , Mr. Murphy , Mr. Reed , Mr. Ricketts , Mr. Rounds , Mr. Sanders , Mr. Scott of Florida , Mrs. Shaheen , Mr. Sheehy , Ms. Smith , Mr. Sullivan , Mr. Wyden , Mr. Young , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Transportation to issue a rule requiring access to AM broadcast stations in passenger motor vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AM Radio for Every Vehicle Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Emergency Management Agency.\n**(2) AM broadcast band**\nThe term AM broadcast band means the band of frequencies between 535 kilohertz and 1705 kilohertz, inclusive.\n**(3) AM broadcast station**\nThe term AM broadcast station means a radio broadcast station\u2014\n**(A)**\nlicensed by the Federal Communications Commission for the dissemination of radio communications intended to be received by the public; and\n**(B)**\noperated on a channel in the AM broadcast band.\n**(4) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(C)**\nthe Committee on Transportation and Infrastructure of the House of Representatives;\n**(D)**\nthe Committee on Homeland Security of the House of Representatives; and\n**(E)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(5) Comptroller General**\nThe term Comptroller General means the Comptroller General of the United States.\n**(6) Device**\nThe term device means a piece of equipment or an apparatus that is designed\u2014\n**(A)**\nto receive signals transmitted by a radio broadcast station; and\n**(B)**\nto play back content or programming derived from those signals.\n**(7) Digital audio AM broadcast station**\n**(A) In general**\nThe term digital audio AM broadcast station means an AM broadcast station that uses an In Band On Channel DAB System (as defined in section 73.402 of title 47, Code of Federal Regulations (or a successor regulation)) for broadcasting purposes.\n**(B) Exclusion**\nThe term digital audio AM broadcast station does not include an All-digital AM station (as defined in section 73.402 of title 47, Code of Federal Regulations (or a successor regulation)).\n**(8) IPAWS**\nThe term IPAWS means the public alert and warning system of the United States described in section 526 of the Homeland Security Act of 2002 ( 6 U.S.C. 321o ).\n**(9) Manufacturer**\nThe term manufacturer has the meaning given the term in section 30102(a) of title 49, United States Code.\n**(10) Passenger motor vehicle**\nThe term passenger motor vehicle has the meaning given the term in section 32101 of title 49, United States Code.\n**(11) Radio broadcast station**\nThe term radio broadcast station has the meaning given the term in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ).\n**(12) Radio station license**\nThe term radio station license has the meaning given the term in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ).\n**(13) Receive**\nThe term receive means to receive a broadcast signal via over-the-air transmission.\n**(14) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(15) Signal**\nThe term signal means radio frequency energy that a holder of a radio station license intentionally emits or causes to be emitted at a specified frequency for the purpose of transmitting content or programming to the public.\n**(16) Standard equipment**\nThe term standard equipment means motor vehicle equipment (as defined in section 30102(a) of title 49, United States Code) that\u2014\n**(A)**\nis installed as a system, part, or component of a passenger motor vehicle as originally manufactured; and\n**(B)**\nthe manufacturer of the passenger motor vehicle recommends or authorizes to be included in the passenger motor vehicle for no additional or separate monetary fee, payment, or surcharge, beyond the base price of the passenger motor vehicle.\n**(17) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n#### 3. AM broadcast stations rule\n##### (a) Rule required\nNot later than 1 year after the date of enactment of this Act, the Secretary, in consultation with the Administrator and the Federal Communications Commission, shall issue a rule\u2014\n**(1)**\nrequiring devices that can receive signals and play content transmitted by AM broadcast stations be installed as standard equipment in passenger motor vehicles\u2014\n**(A)**\nmanufactured in the United States for sale in the United States, imported into the United States, or shipped in interstate commerce; and\n**(B)**\nmanufactured after the effective date of the rule;\n**(2)**\nrequiring access to AM broadcast stations through the devices required under paragraph (1) in a manner that is easily accessible to drivers; and\n**(3)**\nallowing a manufacturer to comply with that rule by installing devices as described in paragraph (1) that can receive signals and play content transmitted by digital audio AM broadcast stations.\n##### (b) Compliance\n**(1) In general**\nExcept as provided in paragraph (2), in issuing the rule required under subsection (a), the Secretary shall establish an effective date for the rule that is not less than 2 years, but not more than 3 years, after the date on which the rule is issued.\n**(2) Certain manufacturers**\nIn issuing the rule required under subsection (a), the Secretary shall establish an effective date for the rule that is at least 4 years after the date on which the rule is issued with respect to manufacturers that manufactured not more than 40,000 passenger motor vehicles for sale in the United States in 2022.\n##### (c) Interim requirement\nFor passenger motor vehicles manufactured after the date of enactment of this Act and manufactured in the United States for sale in the United States, imported into the United States, or shipped in interstate commerce during the period beginning on the day after the date of enactment of this Act and ending on the day before the effective date of the rule issued under subsection (a) that do not include devices that can receive signals and play content transmitted by AM broadcast stations, the manufacturer of the passenger motor vehicles\u2014\n**(1)**\nshall provide clear and conspicuous labeling to inform purchasers of those passenger motor vehicles that the passenger motor vehicles do not include devices that can receive signals and play content transmitted by AM broadcast stations; and\n**(2)**\nmay not charge an additional or separate monetary fee, payment, or surcharge, beyond the base price of the passenger motor vehicles, for access to AM broadcast stations for the period described in this subsection.\n##### (d) Relationship to other laws\nAfter the date of enactment of this Act, a State or a political subdivision of a State may not prescribe or continue in effect a law, regulation, or other requirement applicable to access to AM broadcast stations in passenger motor vehicles.\n##### (e) Enforcement\n**(1) Civil penalty**\nAny person who violates the rule issued under subsection (a) shall be liable to the United States Government for a civil penalty under section 30165(a)(1) of title 49, United States Code, as if that rule were a regulation described in that section.\n**(2) Civil action**\nThe Attorney General may bring a civil action under section 30163 of title 49, United States Code, in an appropriate district court of the United States to enjoin a violation of the rule issued under subsection (a) of this section, as if that rule were a regulation described in subsection (a)(1) of that section 30163.\n##### (f) GAO study\n**(1) In general**\nThe Comptroller General shall conduct a comprehensive study on disseminating emergency alerts and warnings to the public.\n**(2) Requirements**\nThe study required under paragraph (1) shall include\u2014\n**(A)**\nan assessment of\u2014\n**(i)**\nthe role of passenger motor vehicles in IPAWS communications, including by providing access to AM broadcast stations;\n**(ii)**\nthe advantages, effectiveness, limitations, resilience, and accessibility of existing IPAWS communication technologies, including AM broadcast stations in passenger motor vehicles;\n**(iii)**\nthe advantages, effectiveness, limitations, resilience, and accessibility of AM broadcast stations relative to other IPAWS communication technologies in passenger motor vehicles; and\n**(iv)**\nwhether other IPAWS communication technologies are capable of ensuring the President (or a designee) can reach at least 90 percent of the population of the United States at a time of crisis, including at night; and\n**(B)**\na description of any ongoing efforts to integrate new and emerging technologies and communication platforms into the IPAWS framework.\n**(3) Consultation required**\nIn conducting the study required under paragraph (1), the Comptroller General shall consult with\u2014\n**(A)**\nthe Secretary of Homeland Security;\n**(B)**\nthe Federal Communications Commission;\n**(C)**\nthe National Telecommunications and Information Administration;\n**(D)**\nthe Secretary;\n**(E)**\nFederal, State, Tribal, territorial, and local emergency management officials;\n**(F)**\nfirst responders;\n**(G)**\ntechnology experts in resilience and accessibility;\n**(H)**\nradio broadcasters;\n**(I)**\nmanufacturers of passenger motor vehicles; and\n**(J)**\nother relevant stakeholders, as determined by the Comptroller General.\n**(4) Briefing and report**\n**(A) Briefing**\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall brief the appropriate committees of Congress on the results of the study required by paragraph (1), including recommendations for legislation and administrative action as the Comptroller General determines appropriate.\n**(B) Report**\nNot later than 180 days after the date on which the Comptroller General provides the briefing required under subparagraph (A), the Comptroller General shall submit to the appropriate committees of Congress a report describing the results of the study required under paragraph (1), including recommendations for legislation and administrative action as the Comptroller General determines appropriate.\n##### (g) Review\nNot less frequently than once every 5 years after the date on which the Secretary issues the rule required by subsection (a), the Secretary, in coordination with the Administrator and the Federal Communications Commission, shall submit to the appropriate committees of Congress a report that shall include an assessment of\u2014\n**(1)**\nthe impacts of the rule issued under that subsection, including the impacts on public safety; and\n**(2)**\npossible changes to IPAWS communication technologies that would enable resilient and accessible alerts to drivers and passengers of passenger motor vehicles.\n##### (h) Sunset\nThe authority of the Secretary to issue the rule required by subsection (a) shall expire on the date that is 10 years after the date of enactment of this Act.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s315rs.xml",
      "text": "II\nCalendar No. 39\n119th CONGRESS\n1st Session\nS. 315\n[Report No. 119\u201311]\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Markey (for himself, Mr. Cruz , Ms. Baldwin , Mr. Banks , Mr. Barrasso , Mrs. Blackburn , Mr. Blumenthal , Mrs. Britt , Mr. Budd , Ms. Cantwell , Mrs. Capito , Mr. Coons , Mr. Cotton , Mr. Cramer , Mr. Daines , Ms. Ernst , Mrs. Fischer , Mr. Grassley , Ms. Hassan , Mr. Hawley , Ms. Hirono , Mr. Hoeven , Mr. Justice , Mr. King , Ms. Klobuchar , Mr. Lankford , Mr. Luj\u00e1n , Ms. Lummis , Mr. Marshall , Mr. Merkley , Mr. Moran , Mr. Murphy , Mr. Reed , Mr. Ricketts , Mr. Rounds , Mr. Sanders , Mr. Scott of Florida , Mrs. Shaheen , Mr. Sheehy , Ms. Smith , Mr. Sullivan , Mr. Wyden , Mr. Young , Mr. Wicker , Ms. Collins , Mr. Moreno , Ms. Murkowski , Mr. Mullin , Ms. Cortez Masto , Ms. Rosen , Mr. Boozman , Mr. McCormick , Ms. Warren , Mr. Whitehouse , Mr. Crapo , Mr. Ossoff , Mr. Kennedy , Mr. Tuberville , Mrs. Moody , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nApril 3, 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Secretary of Transportation to issue a rule requiring access to AM broadcast stations in passenger motor vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AM Radio for Every Vehicle Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Emergency Management Agency.\n**(2) AM broadcast band**\nThe term AM broadcast band means the band of frequencies between 535 kilohertz and 1705 kilohertz, inclusive.\n**(3) AM broadcast station**\nThe term AM broadcast station means a radio broadcast station\u2014\n**(A)**\nlicensed by the Federal Communications Commission for the dissemination of radio communications intended to be received by the public; and\n**(B)**\noperated on a channel in the AM broadcast band.\n**(4) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(C)**\nthe Committee on Transportation and Infrastructure of the House of Representatives;\n**(D)**\nthe Committee on Homeland Security of the House of Representatives; and\n**(E)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(5) Comptroller General**\nThe term Comptroller General means the Comptroller General of the United States.\n**(6) Device**\nThe term device means a piece of equipment or an apparatus that is designed\u2014\n**(A)**\nto receive signals transmitted by a radio broadcast station; and\n**(B)**\nto play back content or programming derived from those signals.\n**(7) Digital audio AM broadcast station**\n**(A) In general**\nThe term digital audio AM broadcast station means an AM broadcast station that uses an In Band On Channel DAB System (as defined in section 73.402 of title 47, Code of Federal Regulations (or a successor regulation)) for broadcasting purposes.\n**(B) Exclusion**\nThe term digital audio AM broadcast station does not include an All-digital AM station (as defined in section 73.402 of title 47, Code of Federal Regulations (or a successor regulation)).\n**(8) IPAWS**\nThe term IPAWS means the public alert and warning system of the United States described in section 526 of the Homeland Security Act of 2002 ( 6 U.S.C. 321o ).\n**(9) Manufacturer**\nThe term manufacturer has the meaning given the term in section 30102(a) of title 49, United States Code.\n**(10) Passenger motor vehicle**\nThe term passenger motor vehicle has the meaning given the term in section 32101 of title 49, United States Code.\n**(11) Radio broadcast station**\nThe term radio broadcast station has the meaning given the term in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ).\n**(12) Radio station license**\nThe term radio station license has the meaning given the term in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ).\n**(13) Receive**\nThe term receive means to receive a broadcast signal via over-the-air transmission.\n**(14) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(15) Signal**\nThe term signal means radio frequency energy that a holder of a radio station license intentionally emits or causes to be emitted at a specified frequency for the purpose of transmitting content or programming to the public.\n**(16) Standard equipment**\nThe term standard equipment means motor vehicle equipment (as defined in section 30102(a) of title 49, United States Code) that\u2014\n**(A)**\nis installed as a system, part, or component of a passenger motor vehicle as originally manufactured; and\n**(B)**\nthe manufacturer of the passenger motor vehicle recommends or authorizes to be included in the passenger motor vehicle for no additional or separate monetary fee, payment, or surcharge, beyond the base price of the passenger motor vehicle.\n**(17) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n#### 3. AM broadcast stations rule\n##### (a) Rule required\nNot later than 1 year after the date of enactment of this Act, the Secretary, in consultation with the Administrator and the Federal Communications Commission, shall issue a rule\u2014\n**(1)**\nrequiring devices that can receive signals and play content transmitted by AM broadcast stations be installed as standard equipment in passenger motor vehicles\u2014\n**(A)**\nmanufactured in the United States for sale in the United States, imported into the United States, or shipped in interstate commerce; and\n**(B)**\nmanufactured after the effective date of the rule;\n**(2)**\nrequiring access to AM broadcast stations through the devices required under paragraph (1) in a manner that is easily accessible to drivers; and\n**(3)**\nallowing a manufacturer to comply with that rule by installing devices as described in paragraph (1) that can receive signals and play content transmitted by digital audio AM broadcast stations.\n##### (b) Compliance\n**(1) In general**\nExcept as provided in paragraph (2), in issuing the rule required under subsection (a), the Secretary shall establish an effective date for the rule that is not less than 2 years, but not more than 3 years, after the date on which the rule is issued.\n**(2) Certain manufacturers**\nIn issuing the rule required under subsection (a), the Secretary shall establish an effective date for the rule that is at least 4 years after the date on which the rule is issued with respect to manufacturers that manufactured not more than 40,000 passenger motor vehicles for sale in the United States in 2022.\n##### (c) Interim requirement\nFor passenger motor vehicles manufactured after the date of enactment of this Act and manufactured in the United States for sale in the United States, imported into the United States, or shipped in interstate commerce during the period beginning on the day after the date of enactment of this Act and ending on the day before the effective date of the rule issued under subsection (a) that do not include devices that can receive signals and play content transmitted by AM broadcast stations, the manufacturer of the passenger motor vehicles\u2014\n**(1)**\nshall provide clear and conspicuous labeling to inform purchasers of those passenger motor vehicles that the passenger motor vehicles do not include devices that can receive signals and play content transmitted by AM broadcast stations; and\n**(2)**\nmay not charge an additional or separate monetary fee, payment, or surcharge, beyond the base price of the passenger motor vehicles, for access to AM broadcast stations for the period described in this subsection.\n##### (d) Relationship to other laws\nAfter the date of enactment of this Act, a State or a political subdivision of a State may not prescribe or continue in effect a law, regulation, or other requirement applicable to access to AM broadcast stations in passenger motor vehicles.\n##### (e) Enforcement\n**(1) Civil penalty**\nAny person who violates the rule issued under subsection (a) shall be liable to the United States Government for a civil penalty under section 30165(a)(1) of title 49, United States Code, as if that rule were a regulation described in that section.\n**(2) Civil action**\nThe Attorney General may bring a civil action under section 30163 of title 49, United States Code, in an appropriate district court of the United States to enjoin a violation of the rule issued under subsection (a) of this section, as if that rule were a regulation described in subsection (a)(1) of that section 30163.\n##### (f) GAO study\n**(1) In general**\nThe Comptroller General shall conduct a comprehensive study on disseminating emergency alerts and warnings to the public.\n**(2) Requirements**\nThe study required under paragraph (1) shall include\u2014\n**(A)**\nan assessment of\u2014\n**(i)**\nthe role of passenger motor vehicles in IPAWS communications, including by providing access to AM broadcast stations;\n**(ii)**\nthe advantages, effectiveness, limitations, resilience, and accessibility of existing IPAWS communication technologies, including AM broadcast stations in passenger motor vehicles;\n**(iii)**\nthe advantages, effectiveness, limitations, resilience, and accessibility of AM broadcast stations relative to other IPAWS communication technologies in passenger motor vehicles; and\n**(iv)**\nwhether other IPAWS communication technologies are capable of ensuring the President (or a designee) can reach at least 90 percent of the population of the United States at a time of crisis, including at night; and\n**(B)**\na description of any ongoing efforts to integrate new and emerging technologies and communication platforms into the IPAWS framework.\n**(3) Consultation required**\nIn conducting the study required under paragraph (1), the Comptroller General shall consult with\u2014\n**(A)**\nthe Secretary of Homeland Security;\n**(B)**\nthe Federal Communications Commission;\n**(C)**\nthe National Telecommunications and Information Administration;\n**(D)**\nthe Secretary;\n**(E)**\nFederal, State, Tribal, territorial, and local emergency management officials;\n**(F)**\nfirst responders;\n**(G)**\ntechnology experts in resilience and accessibility;\n**(H)**\nradio broadcasters;\n**(I)**\nmanufacturers of passenger motor vehicles; and\n**(J)**\nother relevant stakeholders, as determined by the Comptroller General.\n**(4) Briefing and report**\n**(A) Briefing**\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall brief the appropriate committees of Congress on the results of the study required by paragraph (1), including recommendations for legislation and administrative action as the Comptroller General determines appropriate.\n**(B) Report**\nNot later than 180 days after the date on which the Comptroller General provides the briefing required under subparagraph (A), the Comptroller General shall submit to the appropriate committees of Congress a report describing the results of the study required under paragraph (1), including recommendations for legislation and administrative action as the Comptroller General determines appropriate.\n##### (g) Review\nNot less frequently than once every 5 years after the date on which the Secretary issues the rule required by subsection (a), the Secretary, in coordination with the Administrator and the Federal Communications Commission, shall submit to the appropriate committees of Congress a report that shall include an assessment of\u2014\n**(1)**\nthe impacts of the rule issued under that subsection, including the impacts on public safety; and\n**(2)**\npossible changes to IPAWS communication technologies that would enable resilient and accessible alerts to drivers and passengers of passenger motor vehicles.\n##### (h) Sunset\nThe authority of the Secretary to issue the rule required by subsection (a) shall expire on the date that is 10 years after the date of enactment of this Act.",
      "versionDate": "2025-04-03",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-09-17",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 50 - 1."
      },
      "number": "979",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "AM Radio for Every Vehicle Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-02-13T14:41:24Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-13T14:41:24Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-13T14:41:24Z"
          },
          {
            "name": "Government Accountability Office (GAO)",
            "updateDate": "2025-02-13T14:41:24Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-13T14:41:24Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-02-13T14:41:24Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2025-02-13T14:41:24Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-02-13T14:41:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-05T16:58:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s315",
          "measure-number": "315",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s315v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>AM Radio for Every Vehicle Act of 2025</strong></p><p>This bill requires the Department of Transportation (DOT) to issue a rule requiring AM radio capabilities to be standard in all new passenger\u00a0vehicles. (AM radio is often used to deliver emergency alerts and news and entertainment programming; some newer vehicles do not include AM equipment.)</p><p>Specifically, this bill applies to passenger\u00a0vehicles (1) manufactured in the United States for sale in the United States, imported into the United States, or shipped in interstate commerce; and (2) manufactured\u00a0after the rule's effective date.\u00a0The rule must require all such vehicles to have devices that can receive signals and play content transmitted by AM stations or digital audio AM stations installed as standard equipment and made easily accessible to drivers.</p><p>Prior to the rule's effective date, manufacturers that do not include devices that can access AM radio as standard equipment (1) must inform purchasers of this fact through clear and conspicuous labeling, and (2)\u00a0may not charge an additional or separate fee\u00a0for AM radio access.</p><p>DOT may assess civil penalties for any violation of the rule. The Department of Justice may also bring a civil action to enjoin a violation.</p><p>DOT\u2019s authority to issue the rule expires 10 years after the bill\u2019s enactment.\u00a0</p><p>Further, the Government Accountability Office must study and report on the dissemination of emergency alerts to the public, including by conducting an assessment of AM broadcast stations relative to other Integrated Public Alert and Warning System communication technologies.</p><p>\u00a0</p>"
        },
        "title": "AM Radio for Every Vehicle Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s315.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>AM Radio for Every Vehicle Act of 2025</strong></p><p>This bill requires the Department of Transportation (DOT) to issue a rule requiring AM radio capabilities to be standard in all new passenger\u00a0vehicles. (AM radio is often used to deliver emergency alerts and news and entertainment programming; some newer vehicles do not include AM equipment.)</p><p>Specifically, this bill applies to passenger\u00a0vehicles (1) manufactured in the United States for sale in the United States, imported into the United States, or shipped in interstate commerce; and (2) manufactured\u00a0after the rule's effective date.\u00a0The rule must require all such vehicles to have devices that can receive signals and play content transmitted by AM stations or digital audio AM stations installed as standard equipment and made easily accessible to drivers.</p><p>Prior to the rule's effective date, manufacturers that do not include devices that can access AM radio as standard equipment (1) must inform purchasers of this fact through clear and conspicuous labeling, and (2)\u00a0may not charge an additional or separate fee\u00a0for AM radio access.</p><p>DOT may assess civil penalties for any violation of the rule. The Department of Justice may also bring a civil action to enjoin a violation.</p><p>DOT\u2019s authority to issue the rule expires 10 years after the bill\u2019s enactment.\u00a0</p><p>Further, the Government Accountability Office must study and report on the dissemination of emergency alerts to the public, including by conducting an assessment of AM broadcast stations relative to other Integrated Public Alert and Warning System communication technologies.</p><p>\u00a0</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119s315"
    },
    "title": "AM Radio for Every Vehicle Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>AM Radio for Every Vehicle Act of 2025</strong></p><p>This bill requires the Department of Transportation (DOT) to issue a rule requiring AM radio capabilities to be standard in all new passenger\u00a0vehicles. (AM radio is often used to deliver emergency alerts and news and entertainment programming; some newer vehicles do not include AM equipment.)</p><p>Specifically, this bill applies to passenger\u00a0vehicles (1) manufactured in the United States for sale in the United States, imported into the United States, or shipped in interstate commerce; and (2) manufactured\u00a0after the rule's effective date.\u00a0The rule must require all such vehicles to have devices that can receive signals and play content transmitted by AM stations or digital audio AM stations installed as standard equipment and made easily accessible to drivers.</p><p>Prior to the rule's effective date, manufacturers that do not include devices that can access AM radio as standard equipment (1) must inform purchasers of this fact through clear and conspicuous labeling, and (2)\u00a0may not charge an additional or separate fee\u00a0for AM radio access.</p><p>DOT may assess civil penalties for any violation of the rule. The Department of Justice may also bring a civil action to enjoin a violation.</p><p>DOT\u2019s authority to issue the rule expires 10 years after the bill\u2019s enactment.\u00a0</p><p>Further, the Government Accountability Office must study and report on the dissemination of emergency alerts to the public, including by conducting an assessment of AM broadcast stations relative to other Integrated Public Alert and Warning System communication technologies.</p><p>\u00a0</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119s315"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s315is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s315rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "AM Radio for Every Vehicle Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T11:03:17Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "AM Radio for Every Vehicle Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AM Radio for Every Vehicle Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Transportation to issue a rule requiring access to AM broadcast stations in passenger motor vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T15:18:22Z"
    }
  ]
}
```
