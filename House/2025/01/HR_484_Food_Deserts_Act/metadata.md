# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/484?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/484
- Title: Food Deserts Act
- Congress: 119
- Bill type: HR
- Bill number: 484
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-12-24T09:05:19Z
- Update date including text: 2025-12-24T09:05:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-01-16 - IntroReferral: Sponsor introductory remarks on measure. (CR E41)
- 2025-02-14 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2025-02-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-01-16 - IntroReferral: Sponsor introductory remarks on measure. (CR E41)
- 2025-02-14 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2025-02-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/484",
    "number": "484",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001072",
        "district": "7",
        "firstName": "Andr\u00e9",
        "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
        "lastName": "Carson",
        "party": "D",
        "state": "IN"
      }
    ],
    "title": "Food Deserts Act",
    "type": "HR",
    "updateDate": "2025-12-24T09:05:19Z",
    "updateDateIncludingText": "2025-12-24T09:05:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E41)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:09:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:10:27Z",
                "name": "Referred to"
              }
            },
            "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
            "systemCode": "hsag22"
          },
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:10:27Z",
                "name": "Referred to"
              }
            },
            "name": "Nutrition and Foreign Agriculture Subcommittee",
            "systemCode": "hsag03"
          }
        ]
      },
      "systemCode": "hsag00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "DC"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NV"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CT"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NM"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "HI"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NV"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "OH"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-10",
      "state": "MS"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CO"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MO"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
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
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "AL"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "TX"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "MO"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-29",
      "state": "TX"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "LA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "TX"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MD"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
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
      "sponsorshipDate": "2025-11-04",
      "state": "VA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr484ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 484\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Carson (for himself, Mr. Carter of Louisiana , Mr. Casten , Mrs. Cherfilus-McCormick , Mr. Cohen , Mrs. Watson Coleman , Mrs. Dingell , Mr. Garamendi , Mr. Goldman of New York , Ms. Norton , Mr. Horsford , Mr. Johnson of Georgia , Mr. Krishnamoorthi , Mr. Larson of Connecticut , Mr. Lynch , Mrs. McIver , Mr. Moulton , Mr. Mrvan , Mr. Mullin , Ms. Ross , Ms. Schakowsky , Ms. Scholten , Mr. Soto , Ms. Stansbury , Ms. Stevens , Ms. Tlaib , Mr. Takano , Mr. Tonko , Ms. Tokuda , and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to make grants to States to support the establishment and operation of grocery stores in underserved communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Food Deserts Act .\n#### 2. Grant program to establish grocery stores in underserved communities\n##### (a) Establishment of grant program\nThe Secretary shall establish a program to provide capitalization grants to States for the purpose of establishing revolving funds to support the establishment and operation of grocery stores in underserved communities.\n##### (b) Administration\nA State receiving funds under this Act shall administer the revolving fund of the State through an instrumentality of the State with such powers and limitations as may be required to operate such fund in accordance with the requirements of this Act.\n##### (c) Projects and activities eligible for assistance\nAmounts in a revolving fund shall be used for the purpose of making loans\u2014\n**(1)**\nto open a grocery store in an underserved community, except that such loan may not be used for the purpose of new construction;\n**(2)**\nto support the operations of an existing grocery store in an underserved community;\n**(3)**\nto provide access to healthy food; or\n**(4)**\nto support the operations of a program participant that is located in a community that would be an underserved community if the program participant was not located in such community.\n##### (d) Grocery stores eligible for assistance\n**(1) Required criteria**\nA State receiving a capitalization grant under this Act may only make a loan from the revolving fund of the State to an entity that the State determines\u2014\n**(A)**\nis a grocery store or will be a grocery store after opening;\n**(B)**\nemphasizes or will emphasize unprocessed, healthful foods;\n**(C)**\nprovides or will provide a variety of raw fruits and vegetables;\n**(D)**\nprovides or will provide staple foods;\n**(E)**\nhas a plan to keep such foods in stock to the extent possible;\n**(F)**\ncharge affordable at or below market values;\n**(G)**\neither\u2014\n**(i)**\nis demonstrably qualified to operate a grocery store; or\n**(ii)**\nat the time of such application, has existing partnerships with organizations that provide technical assistance on business operations of food services; and\n**(H)**\nwill match no less than 20 percent, from non-Federal funds, of the amount of such loan.\n**(2) Priority criteria**\nA State shall prioritize an application for a loan from the revolving fund of the State from an entity that the State determines\u2014\n**(A)**\nhires or plans to hire workers who reside within the underserved community that would be served by the entity;\n**(B)**\nprovides or plans to provide classes or other educational information about a healthful diet;\n**(C)**\nsources or plans to source food from local urban farms and gardens; and\n**(D)**\ndemonstrates existing supply chain relationships in the grocery industry.\n##### (e) Application\nAn entity that desires a loan from a revolving fund of a State shall submit an application to the State at such time, in such manner, and containing such information as the State may require.\n##### (f) Loan conditions\n**(1) In general**\nA loan distributed from a revolving fund by a State may be used by a program participant only for the purposes specified in subsection (c).\n**(2) Interest rates**\nA loan distributed by a State from a revolving fund\u2014\n**(A)**\nshall be made at or below market interest rates; and\n**(B)**\nmay be an interest free loan, at terms not to exceed the lesser of 30 years or the projected useful life (as determined by the State) of the project to be financed with the proceeds of the loan.\n**(3) Structure of loan**\nA loan may be distributed from a revolving fund by a State to a program participant in\u2014\n**(A)**\na lump sum; or\n**(B)**\nin multiple distributions over a period of years, if the State determines multiple distributions are necessary to carry out the project.\n**(4) Loan amount**\nA State may not provide a loan to a program participant from the revolving fund of the State in a fiscal year that exceeds 10 percent of the amount available from the fund for making distributions in that fiscal year.\n**(5) Payments**\nAnnual principal and interest payments on a loan received from a revolving fund of a State shall commence not later than 1 year after the loan is disbursed to the program participant and all loans will be fully amortized upon the expiration of the term of the loan.\n**(6) Revenue for repayment**\nA program participant shall establish a dedicated source of revenue for repayment of a loan received from a revolving fund of a State.\n**(7) Crediting revolving fund**\nA revolving fund of a State shall be credited with all payments of principal and interest on all loans made from the revolving fund.\n##### (g) Administration costs\nA State shall charge a program participant an administrative fee of not more than 4 percent of the loan amount. The State shall use the fees to administer the revolving fund and conduct administration activities under this Act.\n##### (h) Technical assistance\nThe Secretary shall provide technical assistance to program participants to assist with sourcing of food, food storage, and other operational requirements.\n##### (i) Bankruptcy\nIn the case of the bankruptcy of a program participant, amounts owed on a loan from a revolving fund shall be afforded precedence over other debt.\n##### (j) Change in underserved status\nIn the case of a community that qualified as underserved during a period in which loans were made by a State pursuant to this section and no longer qualifies as underserved, recipients of loans under this section in such community\u2014\n**(1)**\nshall not be eligible for further loans under this section; and\n**(2)**\nmay not have their loan agreements altered.\n##### (k) Grocery store earnings\nEarnings of a nonprofit organization or municipally owned program participant that are attributable to a loan received from a revolving fund of a State shall be used for reinvestment into the program participant or to support the continuity of operations of the program participant.\n#### 3. Capitalization grants to fund state revolving funds\n##### (a) Eligibility of state for capitalization grant\nTo be eligible for a capitalization grant, a State shall\u2014\n**(1)**\nestablish a revolving fund that complies with the requirements of this Act; and\n**(2)**\nestablish a process for applications and criteria for making loans from the revolving fund, subject to the requirements in section 2(d).\n##### (b) Upon receipt of capitalization grant\nUpon the receipt of a capitalization grant, a State shall deposit such capitalization grant into the revolving fund of the State.\n##### (c) Distribution\nFor a fiscal year, the Secretary shall apportion amounts made available for capitalization grants under this section among the States eligible under subsection (a) in the ratio that\u2014\n**(1)**\nthe population of underserved communities in each State eligible under subsection (a), bears to\n**(2)**\nthe population of underserved communities in all States eligible under subsection (a).\n#### 4. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $150,000,000 for fiscal year 2026.\n#### 5. Definitions\nIn this Act:\n**(1) Capitalization grant**\nThe term capitalization grant means a grant made to a State under the program.\n**(2) Healthful food**\nThe term healthful food means food that reflects the most recent Dietary Guidelines for Americans.\n**(3) Grocery store**\nThe term grocery store means a retail store that derives income primarily from the sale of food for home preparation and consumption.\n**(4) Program**\nThe term program means the program described in section 2(a).\n**(5) Program participant**\nThe term program participant means an entity that has received a loan under the program.\n**(6) Revolving fund**\nThe term revolving fund means a fund established by a State for use as a depository for a capitalization grant.\n**(7) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(8) Staple food**\nThe term staple food has the meaning given the term in section 243(b) of the of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6953(b) ).\n**(9) State**\nThe term State means States of the Union, the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands.\n**(10) Underserved community**\nThe term underserved community has the meaning given the term in section 310B(g)(9)(A) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1932(g)(9)(A) ).",
      "versionDate": "2025-01-16",
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
            "name": "Agricultural marketing and promotion",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Food assistance and relief",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Fruit and vegetables",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-05-20T14:44:35Z"
          },
          {
            "name": "Urban and suburban affairs and development",
            "updateDate": "2025-05-20T14:44:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-02-19T15:30:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr484",
          "measure-number": "484",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr484v00",
            "update-date": "2025-02-24"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Food Deserts Act </strong></p><p>This bill establishes a grant program within the Department of Agriculture to reduce food deserts. Under the program, grants are provided to states for revolving funds that support the establishment and operation of grocery stores in underserved communities. <em>Underserved communities</em> are communities that have (1) limited access to affordable, healthy foods, including fresh fruits and vegetables, in grocery retail stores or farmer-to-consumer direct markets; and (2) a high rate of hunger, a high rate of food insecurity, or a high poverty rate.</p><p>The bill requires states to use such funds for loans that support grocery stores in underserved communities, including for opening a store (excluding new construction), or supporting an existing store.</p><p>In order to qualify for loans, grocery stores must meet criteria enumerated in the bill. For example, grocery stores must (1) emphasize unprocessed, healthful foods; (2) provide staple foods and a variety of raw fruits and vegetables; and (3) charge affordable prices at or below market values.</p><p>Further, states must prioritize loan applications from entities that meet criteria related to</p><ul><li>hiring workers from the underserved community,</li><li>providing classes or educational information about a healthful diet,</li><li>sourcing food from local urban farms and gardens, and</li><li>demonstrating existing supply chain relationships in the grocery industry.</li></ul>"
        },
        "title": "Food Deserts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr484.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Food Deserts Act </strong></p><p>This bill establishes a grant program within the Department of Agriculture to reduce food deserts. Under the program, grants are provided to states for revolving funds that support the establishment and operation of grocery stores in underserved communities. <em>Underserved communities</em> are communities that have (1) limited access to affordable, healthy foods, including fresh fruits and vegetables, in grocery retail stores or farmer-to-consumer direct markets; and (2) a high rate of hunger, a high rate of food insecurity, or a high poverty rate.</p><p>The bill requires states to use such funds for loans that support grocery stores in underserved communities, including for opening a store (excluding new construction), or supporting an existing store.</p><p>In order to qualify for loans, grocery stores must meet criteria enumerated in the bill. For example, grocery stores must (1) emphasize unprocessed, healthful foods; (2) provide staple foods and a variety of raw fruits and vegetables; and (3) charge affordable prices at or below market values.</p><p>Further, states must prioritize loan applications from entities that meet criteria related to</p><ul><li>hiring workers from the underserved community,</li><li>providing classes or educational information about a healthful diet,</li><li>sourcing food from local urban farms and gardens, and</li><li>demonstrating existing supply chain relationships in the grocery industry.</li></ul>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr484"
    },
    "title": "Food Deserts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Food Deserts Act </strong></p><p>This bill establishes a grant program within the Department of Agriculture to reduce food deserts. Under the program, grants are provided to states for revolving funds that support the establishment and operation of grocery stores in underserved communities. <em>Underserved communities</em> are communities that have (1) limited access to affordable, healthy foods, including fresh fruits and vegetables, in grocery retail stores or farmer-to-consumer direct markets; and (2) a high rate of hunger, a high rate of food insecurity, or a high poverty rate.</p><p>The bill requires states to use such funds for loans that support grocery stores in underserved communities, including for opening a store (excluding new construction), or supporting an existing store.</p><p>In order to qualify for loans, grocery stores must meet criteria enumerated in the bill. For example, grocery stores must (1) emphasize unprocessed, healthful foods; (2) provide staple foods and a variety of raw fruits and vegetables; and (3) charge affordable prices at or below market values.</p><p>Further, states must prioritize loan applications from entities that meet criteria related to</p><ul><li>hiring workers from the underserved community,</li><li>providing classes or educational information about a healthful diet,</li><li>sourcing food from local urban farms and gardens, and</li><li>demonstrating existing supply chain relationships in the grocery industry.</li></ul>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr484"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr484ih.xml"
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
      "title": "Food Deserts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Food Deserts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T13:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to make grants to States to support the establishment and operation of grocery stores in underserved communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T13:18:22Z"
    }
  ]
}
```
