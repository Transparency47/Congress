# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/237
- Title: Honoring Our Fallen Heroes Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 237
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-01-21T05:02:01Z
- Update date including text: 2026-01-21T05:02:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 78.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 78.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/237",
    "number": "237",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Honoring Our Fallen Heroes Act of 2025",
    "type": "S",
    "updateDate": "2026-01-21T05:02:01Z",
    "updateDateIncludingText": "2026-01-21T05:02:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 78.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
            "date": "2025-05-20T20:22:13Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-15T17:30:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-23T23:03:41Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ND"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WY"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "DE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NE"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SC"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "HI"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NH"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ND"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-01-27",
      "state": "GA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "WA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "LA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "OR"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NJ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NV"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
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
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "VA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MD"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "NC"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "KS"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "AK"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MD"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MO"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "PA"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "ID"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "KS"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "ID"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-28",
      "state": "VT"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "MO"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NV"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
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
      "sponsorshipDate": "2025-07-31",
      "state": "ME"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NM"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s237is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 237\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Ms. Klobuchar (for herself, Mr. Cramer , Mr. Banks , Mr. Barrasso , Mrs. Blackburn , Mr. Blumenthal , Mr. Coons , Mr. Cornyn , Mr. Cruz , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mrs. Fischer , Mr. Graham , Ms. Hirono , Mr. Justice, Mr. Kelly , Mr. Markey , Mr. Padilla , Mr. Rounds , Mr. Schiff , Mrs. Shaheen , Mr. Sheehy , Ms. Smith , Mr. Warner , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide public safety officer benefits for exposure-related cancers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honoring Our Fallen Heroes Act of 2025 .\n#### 2. Honoring our fallen heroes\n##### (a) Cancer-Related deaths and disabilities\n**(1) In general**\nSection 1201 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 ) is amended by adding at the end the following:\n(p) Exposure-Related cancers (1) Definitions In this subsection: (A) Carcinogen The term carcinogen means an agent that is\u2014 (i) classified by the International Agency for Research on Cancer under Group 1 or Group 2A; and (ii) reasonably linked to an exposure-related cancer. (B) Director The term Director means the Director of the Bureau. (C) Exposure-related cancer As updated from time to time in accordance with paragraph (3), the term exposure-related cancer means\u2014 (i) bladder cancer; (ii) brain cancer; (iii) breast cancer; (iv) cervical cancer; (v) colon cancer; (vi) colorectal cancer; (vii) esophageal cancer; (viii) kidney cancer; (ix) leukemia; (x) lung cancer; (xi) malignant melanoma; (xii) mesothelioma; (xiii) multiple myeloma; (xiv) non-Hodgkins lymphoma; (xv) ovarian cancer; (xvi) prostate cancer; (xvii) skin cancer; (xviii) stomach cancer; (xix) testicular cancer; (xx) thyroid cancer; (xxi) any form of cancer that is considered a WTC-related health condition under section 3312(a) of the Public Health Service Act ( 42 U.S.C. 300mm\u201322(a) ); and (xxii) any form of cancer added to this definition pursuant to an update in accordance with paragraph (3). (2) Personal injury sustained in the line of duty (A) In general Subject to subparagraph (B), as determined by the Bureau, the exposure of a public safety officer to a carcinogen shall be presumed to constitute a personal injury within the meaning of subsection (a) or (b) sustained in the line of duty by the officer and directly and proximately resulting in death or permanent and total disability, if\u2014 (i) the exposure occurred while the public safety officer was engaged in line of duty action or activity; (ii) the public safety officer began serving as a public safety officer not fewer than 5 years before the date of the diagnosis of the public safety officer with an exposure-related cancer; (iii) the public safety officer was diagnosed with the exposure-related cancer not more than 15 years after the public safety officer\u2019s last date of active service as a public safety officer; and (iv) the exposure-related cancer directly and proximately results in the death or permanent and total disability of the public safety officer. (B) Exception The presumption under subparagraph (A) shall not apply if competent medical evidence establishes that the exposure of the public safety officer to the carcinogen was not a substantial contributing factor in the death or disability of the public safety officer. (3) Additional exposure-related cancers (A) In general From time to time but not less frequently than once every 3 years, the Director shall\u2014 (i) review the definition of exposure-related cancer under paragraph (1); and (ii) if appropriate, update the definition, in accordance with this paragraph\u2014 (I) by rule; or (II) by publication in the Federal Register or on the public website of the Bureau. (B) Basis for updates (i) In general The Director shall make an update under subparagraph (A)(ii) in any case in which the Director finds such an update to be appropriate based on competent medical evidence of significant risk to public safety officers of developing the form of exposure-related cancer that is the subject of the update from engagement in their public safety activities. (ii) Evidence The competent medical evidence described in clause (i) may include recommendations, risk assessments, and scientific studies by\u2014 (I) the National Institute for Occupational Safety and Health; (II) the National Toxicology Program; (III) the National Academies of Sciences, Engineering, and Medicine; or (IV) the International Agency for Research on Cancer. (C) Petitions to add to the list of exposure-related cancers (i) In general Any person may petition the Director to add a form of cancer to the definition of exposure-related cancer under paragraph (1). (ii) Content of petition A petition under clause (i) shall provide information to show that there is sufficient competent medical evidence of significant risk to public safety officers of developing the cancer from engagement in their public safety activities. (iii) Timely and substantive decisions (I) Referral Not later than 180 days after receipt of a petition satisfying clause (ii), the Director shall refer the petition to appropriate medical experts for review, analysis (including risk assessment and scientific study), and recommendation. (II) Consideration The Director shall consider each recommendation under subclause (I) and promptly take appropriate action in connection with the recommendation pursuant to subparagraph (B). (iv) Notification to congress Not later than 30 days after taking any substantive action in connection with a recommendation under clause (iii)(II), the Director shall notify the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives of the substantive action. .\n**(2) Applicability**\nThe amendment made by paragraph (1) shall apply to any claim under\u2014\n**(A)**\nsection 1201(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281(a) ) that is predicated upon the death of a public safety officer on or after January 1, 2020, that is the direct and proximate result of an exposure-related cancer; or\n**(B)**\nsection 1201(b) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281(b) ) that is filed on or after January 1, 2020, and predicated upon a disability that is the direct and proximate result of an exposure-related cancer.\n**(3) Time for filing claim**\nNotwithstanding any other provision of law, an individual who desires to file a claim that is predicated upon the amendment made by paragraph (1) shall not be precluded from filing such a claim within 3 years of the date of enactment of this Act.\n##### (b) Confidentiality of information\n**(1) In general**\nSection 812(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10231(a) ) is amended\u2014\n**(A)**\nin the first sentence, by striking furnished under this title by any person and identifiable to any specific private person and inserting furnished under any law to any component of the Office of Justice Programs, or furnished otherwise under this title, by any entity or person, including any information identifiable to any specific private person, ; and\n**(B)**\nin the second sentence, by striking person furnishing such information and inserting entity or person furnishing such information or to whom such information pertains .\n**(2) Effective date; applicability**\nThe amendments made by paragraph (1) shall\u2014\n**(A)**\nshall take effect for all purposes as if enacted on December 27, 1979; and\n**(B)**\napply to any matter pending, before the Department of Justice or otherwise, as of the date of enactment of this Act.\n##### (c) Technical amendments\n**(1) In general**\nSection 1201(o)(2) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281(o)(2) ) is amended\u2014\n**(A)**\nin subparagraph (A), by inserting or (b) after subsection (a) ;\n**(B)**\nin subparagraph (B), by inserting or (b) after subsection (a) ; and\n**(C)**\nin subparagraph (C), by inserting or (b) after subsection (a) .\n**(2) Applicability**\nThe amendments made by paragraph (1) shall apply to any matter pending before the Department of Justice as of the date of enactment of this Act.\n#### 3. Technical amendments\n##### (a) In general\nSection 3 of the Safeguarding America\u2019s First Responders Act of 2020 ( 34 U.S.C. 10281 note) is amended by adding at the end the following:\n(d) Definition In this section, the term line of duty action includes any action\u2014 (1) in which a public safety officer engaged at the direction of the agency served by the public safety officer; or (2) the public safety officer is authorized or obligated to perform. .\n##### (b) Applicability\n**(1) In general**\nThe amendment made by subsection (a) shall apply to any claim under section 3 of the Safeguarding America\u2019s First Responders Act of 2020 ( 34 U.S.C. 10281 note)\u2014\n**(A)**\nthat is predicated upon the death of a public safety officer on or after January 1, 2020; or\n**(B)**\nthat is\u2014\n**(i)**\npredicated upon the disability of a public safety officer; and\n**(ii)**\nfiled on or after January 1, 2020.\n**(2) Time for filing claim**\nNotwithstanding any other provision of law, an individual who desires to file a claim that is predicated upon the amendment made by subsection (a) shall not be precluded from filing such a claim within 3 years of the date of enactment of this Act.",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s237rs.xml",
      "text": "II\nCalendar No. 78\n119th CONGRESS\n1st Session\nS. 237\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Ms. Klobuchar (for herself, Mr. Cramer , Mr. Banks , Mr. Barrasso , Mrs. Blackburn , Mr. Blumenthal , Mr. Coons , Mr. Cornyn , Mr. Cruz , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mrs. Fischer , Mr. Graham , Ms. Hirono , Mr. Justice, Mr. Kelly , Mr. Markey , Mr. Padilla , Mr. Rounds , Mr. Schiff , Mrs. Shaheen , Mr. Sheehy , Ms. Smith , Mr. Warner , Ms. Warren , Mr. Welch , Mr. Whitehouse , Mr. Wyden , Mr. Hoeven , Mr. Ossoff , Mrs. Capito , Ms. Cantwell , Mr. Gallego , Mr. Moreno , Mr. Kennedy , Mr. Merkley , Mr. Kim , Ms. Rosen , Mrs. Moody , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide public safety officer benefits for exposure-related cancers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honoring Our Fallen Heroes Act of 2025 .\n#### 2. Honoring our fallen heroes\n##### (a) Cancer-Related deaths and disabilities\n**(1) In general**\nSection 1201 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281 ) is amended by adding at the end the following:\n(p) Exposure-Related cancers (1) Definitions In this subsection: (A) Carcinogen The term carcinogen means an agent that is\u2014 (i) classified by the International Agency for Research on Cancer under Group 1 or Group 2A; and (ii) reasonably linked to an exposure-related cancer. (B) Director The term Director means the Director of the Bureau. (C) Exposure-related cancer As updated from time to time in accordance with paragraph (3), the term exposure-related cancer means\u2014 (i) bladder cancer; (ii) brain cancer; (iii) breast cancer; (iv) cervical cancer; (v) colon cancer; (vi) colorectal cancer; (vii) esophageal cancer; (viii) kidney cancer; (ix) leukemia; (x) lung cancer; (xi) malignant melanoma; (xii) mesothelioma; (xiii) multiple myeloma; (xiv) non-Hodgkins lymphoma; (xv) ovarian cancer; (xvi) prostate cancer; (xvii) skin cancer; (xviii) stomach cancer; (xix) testicular cancer; (xx) thyroid cancer; (xxi) any form of cancer that is considered a WTC-related health condition under section 3312(a) of the Public Health Service Act ( 42 U.S.C. 300mm\u201322(a) ); and (xxii) any form of cancer added to this definition pursuant to an update in accordance with paragraph (3). (2) Personal injury sustained in the line of duty (A) In general Subject to subparagraph (B), as determined by the Bureau, the exposure of a public safety officer to a carcinogen shall be presumed to constitute a personal injury within the meaning of subsection (a) or (b) sustained in the line of duty by the officer and directly and proximately resulting in death or permanent and total disability, if\u2014 (i) the exposure occurred while the public safety officer was engaged in line of duty action or activity; (ii) the public safety officer began serving as a public safety officer not fewer than 5 years before the date of the diagnosis of the public safety officer with an exposure-related cancer; (iii) the public safety officer was diagnosed with the exposure-related cancer not more than 15 years after the public safety officer\u2019s last date of active service as a public safety officer; and (iv) the exposure-related cancer directly and proximately results in the death or permanent and total disability of the public safety officer. (B) Exception The presumption under subparagraph (A) shall not apply if competent medical evidence establishes that the exposure of the public safety officer to the carcinogen was not a substantial contributing factor in the death or disability of the public safety officer. (3) Additional exposure-related cancers (A) In general From time to time but not less frequently than once every 3 years, the Director shall\u2014 (i) review the definition of exposure-related cancer under paragraph (1); and (ii) if appropriate, update the definition, in accordance with this paragraph\u2014 (I) by rule; or (II) by publication in the Federal Register or on the public website of the Bureau. (B) Basis for updates (i) In general The Director shall make an update under subparagraph (A)(ii) in any case in which the Director finds such an update to be appropriate based on competent medical evidence of significant risk to public safety officers of developing the form of exposure-related cancer that is the subject of the update from engagement in their public safety activities. (ii) Evidence The competent medical evidence described in clause (i) may include recommendations, risk assessments, and scientific studies by\u2014 (I) the National Institute for Occupational Safety and Health; (II) the National Toxicology Program; (III) the National Academies of Sciences, Engineering, and Medicine; or (IV) the International Agency for Research on Cancer. (C) Petitions to add to the list of exposure-related cancers (i) In general Any person may petition the Director to add a form of cancer to the definition of exposure-related cancer under paragraph (1). (ii) Content of petition A petition under clause (i) shall provide information to show that there is sufficient competent medical evidence of significant risk to public safety officers of developing the cancer from engagement in their public safety activities. (iii) Timely and substantive decisions (I) Referral Not later than 180 days after receipt of a petition satisfying clause (ii), the Director shall refer the petition to appropriate medical experts for review, analysis (including risk assessment and scientific study), and recommendation. (II) Consideration The Director shall consider each recommendation under subclause (I) and promptly take appropriate action in connection with the recommendation pursuant to subparagraph (B). (iv) Notification to congress Not later than 30 days after taking any substantive action in connection with a recommendation under clause (iii)(II), the Director shall notify the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives of the substantive action. .\n**(2) Applicability**\nThe amendment made by paragraph (1) shall apply to any claim under\u2014\n**(A)**\nsection 1201(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281(a) ) that is predicated upon the death of a public safety officer on or after January 1, 2020, that is the direct and proximate result of an exposure-related cancer; or\n**(B)**\nsection 1201(b) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281(b) ) that is filed on or after January 1, 2020, and predicated upon a disability that is the direct and proximate result of an exposure-related cancer.\n**(3) Time for filing claim**\nNotwithstanding any other provision of law, an individual who desires to file a claim that is predicated upon the amendment made by paragraph (1) shall not be precluded from filing such a claim within 3 years of the date of enactment of this Act.\n##### (b) Confidentiality of information\n**(1) In general**\nSection 812(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10231(a) ) is amended\u2014\n**(A)**\nin the first sentence, by striking furnished under this title by any person and identifiable to any specific private person and inserting furnished under any law to any component of the Office of Justice Programs, or furnished otherwise under this title, by any entity or person, including any information identifiable to any specific private person, ; and\n**(B)**\nin the second sentence, by striking person furnishing such information and inserting entity or person furnishing such information or to whom such information pertains .\n**(2) Effective date; applicability**\nThe amendments made by paragraph (1) shall\u2014\n**(A)**\nshall take effect for all purposes as if enacted on December 27, 1979; and\n**(B)**\napply to any matter pending, before the Department of Justice or otherwise, as of the date of enactment of this Act.\n##### (c) Technical amendments\n**(1) In general**\nSection 1201(o)(2) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10281(o)(2) ) is amended\u2014\n**(A)**\nin subparagraph (A), by inserting or (b) after subsection (a) ;\n**(B)**\nin subparagraph (B), by inserting or (b) after subsection (a) ; and\n**(C)**\nin subparagraph (C), by inserting or (b) after subsection (a) .\n**(2) Applicability**\nThe amendments made by paragraph (1) shall apply to any matter pending before the Department of Justice as of the date of enactment of this Act.\n#### 3. Technical amendments\n##### (a) In general\nSection 3 of the Safeguarding America\u2019s First Responders Act of 2020 ( 34 U.S.C. 10281 note) is amended by adding at the end the following:\n(d) Definition In this section, the term line of duty action includes any action\u2014 (1) in which a public safety officer engaged at the direction of the agency served by the public safety officer; or (2) the public safety officer is authorized or obligated to perform. .\n##### (b) Applicability\n**(1) In general**\nThe amendment made by subsection (a) shall apply to any claim under section 3 of the Safeguarding America\u2019s First Responders Act of 2020 ( 34 U.S.C. 10281 note)\u2014\n**(A)**\nthat is predicated upon the death of a public safety officer on or after January 1, 2020; or\n**(B)**\nthat is\u2014\n**(i)**\npredicated upon the disability of a public safety officer; and\n**(ii)**\nfiled on or after January 1, 2020.\n**(2) Time for filing claim**\nNotwithstanding any other provision of law, an individual who desires to file a claim that is predicated upon the amendment made by subsection (a) shall not be precluded from filing such a claim within 3 years of the date of enactment of this Act.",
      "versionDate": "2025-05-20",
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1269",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Honoring Our Fallen Heroes Act of 2025",
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
            "name": "Cancer",
            "updateDate": "2025-03-21T19:58:04Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-21T19:58:04Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-03-21T19:58:04Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-21T19:58:04Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-21T19:58:04Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-03-21T19:58:04Z"
          },
          {
            "name": "Worker safety and health",
            "updateDate": "2025-03-21T19:58:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-24T14:34:38Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s237is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s237rs.xml"
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
      "title": "Honoring Our Fallen Heroes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:03:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Honoring Our Fallen Heroes Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Honoring Our Fallen Heroes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide public safety officer benefits for exposure-related cancers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:49Z"
    }
  ]
}
```
