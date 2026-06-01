# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1518?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1518
- Title: New Era of Preventing End-Stage Kidney Disease Act
- Congress: 119
- Bill type: HR
- Bill number: 1518
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-04-23T08:06:51Z
- Update date including text: 2026-04-23T08:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-24 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1518",
    "number": "1518",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "New Era of Preventing End-Stage Kidney Disease Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:06:51Z",
    "updateDateIncludingText": "2026-04-23T08:06:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:05:10Z",
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
          "date": "2025-02-24T17:05:05Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "AL"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "WV"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
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
      "sponsorshipDate": "2025-05-07",
      "state": "DC"
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
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NC"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "SC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "MI"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "NY"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "GA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CO"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "FL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "CA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
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
      "sponsorshipDate": "2025-08-12",
      "state": "NC"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NJ"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "DE"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MD"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MI"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "OH"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NE"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "TX"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NM"
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
      "sponsorshipDate": "2026-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "NV"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-06",
      "state": "MS"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NY"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "TX"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "WI"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "OR"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CA"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1518ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1518\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Bilirakis (for himself, Ms. Sewell , Mrs. Miller of West Virginia , Mr. Peters , Mr. Balderson , Mr. Tonko , Mr. Schneider , and Mr. Davis of Illinois ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Public Health Service Act with respect to preventing end-stage kidney disease, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the New Era of Preventing End-Stage Kidney Disease Act .\n#### 2. Centers of Excellence on Rare Kidney Disease Research in the National Institute of Diabetes and Digestive and Kidney Diseases\nSubpart 3 of part C of title IV of the Public Health Service Act ( 42 U.S.C. 281 et seq. ) is amended by inserting after section 426 ( 42 U.S.C. 285c ) the following new section:\n426A. Centers of Excellence on Rare Kidney Disease Research in the National Institute of Diabetes and Digestive and Kidney Diseases (a) Cooperative agreements and grants (1) In general The Director of the Institute may enter into cooperative agreements with, and make grants to, public and private nonprofit entities to pay all or part of the cost of planning, establishing, or strengthening, and providing basic operating support for, regional centers of excellence for rare kidney diseases, including primary glomerular disease. Such centers of excellence shall be known as NIDDK Centers of Excellence on Rare Kidney Disease Research (referred to in this section as Centers of Excellence ). (2) Purposes of centers The purposes of the Centers of Excellence funded pursuant to paragraph (1) shall be\u2014 (A) to conduct research on the causes, etiology, symptoms, diagnosis, progression, and treatment of rare kidney diseases, including glomerular diseases; (B) to increase public awareness of rare kidney diseases, particularly in rural and underserved communities; and (C) to develop resources for clinical research into, training in, and demonstration of diagnostic, prevention, control, and treatment methods for, rare kidney diseases. (3) Policies A cooperative agreement or grant under paragraph (1) shall be entered into in accordance with policies established by the Director of the National Institutes of Health. (b) Coordination with other institutes The Director of the Institute shall coordinate the activities under this section with similar activities that are related to rare kidney disease and conducted by other national research institutes, centers, and agencies of the National Institutes of Health and by the Food and Drug Administration. (c) Use of funds An entity that enters into a cooperative agreement or receives a grant under subsection (a) may use funds received through such agreement or grant\u2014 (1) to cover patient care costs required to conduct research described in subsection (a)(2)(A); (2) to provide, for the purpose described in subsection (a)(2)(B)\u2014 (A) clinical training and continuing education for health professionals and related personnel with respect to rare kidney diseases; and (B) information programs for the public, with respect to rare kidney diseases; and (3) to provide, for the purpose described in subsection (a)(2)(B)\u2014 (A) for education of members of the public, particularly through outreach to rural and underserved communities, on the diagnosis (including through routine urinalysis and through genetic testing), prevention, control, and treatment of rare kidney diseases; and (B) for education of individuals diagnosed with rare kidney diseases on renal diet and lifestyle, genetic testing, and programs to promote urinalysis, and on mental and emotional health resources for families of rare kidney disease patients. (d) Research funded Research conducted using funds awarded through a cooperative agreement or grant under this section\u2014 (1) shall include study of genotype-phenotype relation to disease progression; and (2) with respect the populations studied in such research, may not include any consideration of quality-adjusted life years or disability adjusted life years, or other similar mechanisms that discriminate against individuals with disabilities in value and cost-effectiveness assessments. (e) Period of support; additional periods The period of support for a center of excellence under subsection (a) may not exceed 5 years, except that such period may be extended by the Director of the Institute for additional periods of not more than 5 years for each center if\u2014 (1) the operations of such center have been reviewed by an appropriate technical and scientific peer review group established by the Director of the Institute; and (2) such group has recommended to the Director of the Institute that such period should be extended. (f) Authorization of appropriations To carry out this section, there are authorized to be appropriated $6,000,000 for each of fiscal years 2026 through 2030. .\n#### 3. Understanding and Slowing the Progression of Rare Kidney Disease Through Early Intervention, Testing, and Treatment\n##### (a) In general\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall conduct a study on testing, preventative care, precision medicine, and treatment, with respect to rare kidney disease. Such study shall review\u2014\n**(1)**\nthe impact of routine urinalysis on the timely diagnosis of rare kidney disease and on the quality of patient care following a diagnosis of such disease;\n**(2)**\nthe quality and reliability of kidney biopsy in the diagnosis of rare kidney disease;\n**(3)**\nthe utility and appropriate use of genetic and genomic tests in detecting kidney disease, including\u2014\n**(A)**\nadvances in genetic and genomic testing, and in particular testing of the APOL1 gene, and whether such testing may improve the diagnosis and treatment of rare kidney disease;\n**(B)**\nbarriers to genetic and genomic testing, such as diagnostic, predictive, presymptomatic testing, and DNA sequencing clinical services, including an analysis of any existing barriers related to health insurance coverage of such testing and access to genetic counselors, pathologists, and other relevant professions; and\n**(C)**\nstrategies to increase routine urinalysis and other diagnostic testing and to improve technologies to diagnose such disease, including genetic testing, and to improve access to health insurance coverage of such diagnostic testing and technologies;\n**(4)**\nthe social, behavioral, and biological factors leading to rare kidney disease;\n**(5)**\ntreatment patterns associated with providing care, under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), the Medicaid program under title XIX of such Act ( 42 U.S.C. 1396 et seq. ), and through private health insurance, to populations that are disproportionately affected by such disease;\n**(6)**\naccess to nephrologists among populations that are disproportionately affected by such disease;\n**(7)**\nongoing efforts and recommendations to slow the progression of end-stage kidney disease in populations that are disproportionately affected by rare kidney disease; and\n**(8)**\npatient trust of treating providers among populations that are disproportionately affected by such disease.\n##### (b) Report\n**(1) In general**\nNot later than 18 months after the date of the enactment of this Act, the Secretary shall submit to the Congress a report on the results of the study under subsection (a), together with such recommendations as the Secretary determines to be appropriate.\n**(2) Consultation**\nIn conducting the study under subsection (a) and developing the report required by paragraph (1), the Secretary shall consult with relevant stakeholders, including health care providers, medical professional societies, State-based societies, public health experts, health educators, health professional organizations, drug and device manufacturers, patient organizations, pharmacists, payors, State and local public health departments, State medical boards, and other entities with experience in health care, public health, nephrology, and rare disease, as appropriate.\n##### (c) Coordination\nIn carrying out the activities under subsections (a) and (b), the Secretary shall coordinate with the Director of NIH, the Administrator of the Center for Medicare & Medicaid Services, the Administrator of the Health Resources and Services Administration, and the Director of the Center for Medicare and Medicaid Innovation.\n##### (d) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $1,000,000 for each of fiscal years 2026 through 2030.\n#### 4. Provider education\n##### (a) Primary care training\nSection 747(b)(3)(E) of the Public Health Service Act ( 42 U.S.C. 293k(b)(3)(E) ) is amended\u2014\n**(1)**\nby striking and individuals and inserting , individuals ; and\n**(2)**\nby inserting , and individuals with kidney disease (including rare kidney disease) after disabilities .\n##### (b) Nephrology fellowships\nSection 736(b) of the Public Health Service Act ( 42 U.S.C. 293 ) is amended\u2014\n**(1)**\nby redesignating paragraph (7) as paragraph (8);\n**(2)**\nin paragraph (6)(B), by striking ; and and inserting a semicolon; and\n**(3)**\nby inserting after paragraph (6) the following:\n(7) to award fellowships, which may include stipends, for postgraduate training in the field of nephrology, for the purposes of\u2014 (A) increasing providers\u2019 knowledge of issues related to prevention, diagnosis, and treatment of rare kidney disease for populations disproportionately impacted by the disease, including the prevalence of the gene APOL1; (B) improving the quality of rare kidney disease prevention, diagnosis, and treatment delivered to racial and ethnic minorities; and (C) increasing the number of nephrologists trained to provide care to such populations; and .\n#### 5. Delaying kidney disease impact\nSection 1881(f) of the Social Security Act ( 42 U.S.C. 1395rr(f) ) is amended by adding at the end the following new paragraph:\n(9) (A) The Secretary shall conduct experiments to evaluate methods for treating rare kidney disease, giving particular attention to treatments that would delay or eliminate the need for dialysis and transplant. (B) The Secretary shall conduct a comprehensive study of methods to increase public awareness of rare kidney disease. (C) The Secretary shall submit to Congress, not later than 24 months after the date of the enactment of the New Era of Preventing End-Stage Kidney Disease Act, a report on the experiments and study conducted under subparagraphs (A) and (B). Such report shall include recommendations for legislative changes that the Secretary finds necessary or desirable as a result of such experiments and study. .",
      "versionDate": "2025-02-24",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Digestive and metabolic diseases",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Genetics",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-07-17T18:44:13Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-07-17T18:44:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T15:52:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1518",
          "measure-number": "1518",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-08-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1518v00",
            "update-date": "2025-08-13"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>New Era of Preventing End-Stage Kidney Disease Act</strong></p><p>This bill establishes regional centers of excellence, postgraduate fellowships, and training for health professionals relating to the diagnosis and treatment of rare kidney disease. It also requires the Department of Health and Human Services (HHS) to conduct various studies on rare kidney disease.</p><p>Specifically, it authorizes the National Institute of Diabetes and Digestive and Kidney Diseases to award funding to public and private nonprofit entities for establishing regional centers of excellence that will increase public awareness, conduct research, and develop resources for diagnosing and treating rare kidney diseases. A center may receive such funding for up to five years, unless extended by the institute.\u00a0</p><p>The bill also requires health professions schools receiving a grant from the Health Resources and Services Administration (HRSA) Centers of Excellence program to award fellowships for training on preventing, diagnosing, and treating rare kidney disease in disproportionately impacted populations.</p><p>Also, the bill expands the priorities of\u00a0HRSA\u2019s Primary Care Training and Enhancement program to include training for health care workers to care for individuals with kidney disease.</p><p>Additionally,\u00a0HHS must conduct several studies and report to Congress on topics such as treating rare kidney disease in disproportionately affected populations, eliminating the need for dialysis or kidney transplants, and increasing public awareness of rare kidney disease.</p>"
        },
        "title": "New Era of Preventing End-Stage Kidney Disease Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1518.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>New Era of Preventing End-Stage Kidney Disease Act</strong></p><p>This bill establishes regional centers of excellence, postgraduate fellowships, and training for health professionals relating to the diagnosis and treatment of rare kidney disease. It also requires the Department of Health and Human Services (HHS) to conduct various studies on rare kidney disease.</p><p>Specifically, it authorizes the National Institute of Diabetes and Digestive and Kidney Diseases to award funding to public and private nonprofit entities for establishing regional centers of excellence that will increase public awareness, conduct research, and develop resources for diagnosing and treating rare kidney diseases. A center may receive such funding for up to five years, unless extended by the institute.\u00a0</p><p>The bill also requires health professions schools receiving a grant from the Health Resources and Services Administration (HRSA) Centers of Excellence program to award fellowships for training on preventing, diagnosing, and treating rare kidney disease in disproportionately impacted populations.</p><p>Also, the bill expands the priorities of\u00a0HRSA\u2019s Primary Care Training and Enhancement program to include training for health care workers to care for individuals with kidney disease.</p><p>Additionally,\u00a0HHS must conduct several studies and report to Congress on topics such as treating rare kidney disease in disproportionately affected populations, eliminating the need for dialysis or kidney transplants, and increasing public awareness of rare kidney disease.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119hr1518"
    },
    "title": "New Era of Preventing End-Stage Kidney Disease Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>New Era of Preventing End-Stage Kidney Disease Act</strong></p><p>This bill establishes regional centers of excellence, postgraduate fellowships, and training for health professionals relating to the diagnosis and treatment of rare kidney disease. It also requires the Department of Health and Human Services (HHS) to conduct various studies on rare kidney disease.</p><p>Specifically, it authorizes the National Institute of Diabetes and Digestive and Kidney Diseases to award funding to public and private nonprofit entities for establishing regional centers of excellence that will increase public awareness, conduct research, and develop resources for diagnosing and treating rare kidney diseases. A center may receive such funding for up to five years, unless extended by the institute.\u00a0</p><p>The bill also requires health professions schools receiving a grant from the Health Resources and Services Administration (HRSA) Centers of Excellence program to award fellowships for training on preventing, diagnosing, and treating rare kidney disease in disproportionately impacted populations.</p><p>Also, the bill expands the priorities of\u00a0HRSA\u2019s Primary Care Training and Enhancement program to include training for health care workers to care for individuals with kidney disease.</p><p>Additionally,\u00a0HHS must conduct several studies and report to Congress on topics such as treating rare kidney disease in disproportionately affected populations, eliminating the need for dialysis or kidney transplants, and increasing public awareness of rare kidney disease.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119hr1518"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1518ih.xml"
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
      "title": "New Era of Preventing End-Stage Kidney Disease Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New Era of Preventing End-Stage Kidney Disease Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act with respect to preventing end-stage kidney disease, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T12:18:38Z"
    }
  ]
}
```
