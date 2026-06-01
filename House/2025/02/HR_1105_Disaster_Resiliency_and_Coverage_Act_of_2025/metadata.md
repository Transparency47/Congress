# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1105
- Title: Disaster Resiliency and Coverage Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1105
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2026-05-11T20:11:26Z
- Update date including text: 2026-05-11T20:11:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1105",
    "number": "1105",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Disaster Resiliency and Coverage Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-11T20:11:26Z",
    "updateDateIncludingText": "2026-05-11T20:11:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:07:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-06T22:15:31Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-06T15:07:25Z",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "HI"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
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
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "DC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "WA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-06",
      "state": "HI"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NM"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-30",
      "state": "AL"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MN"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "PA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-11-04",
      "state": "IL"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MI"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MI"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1105ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1105\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. Thompson of California (for himself, Mr. LaMalfa , Mrs. Kim , Mr. Obernolte , Mr. Valadao , Ms. Barrag\u00e1n , Ms. Brownley , Mr. Carbajal , Mr. Carter of Louisiana , Mr. Case , Ms. Castor of Florida , Ms. Chu , Mr. Cisneros , Mr. Costa , Mr. Fields , Ms. Lois Frankel of Florida , Mr. Frost , Mr. Garamendi , Mr. Goldman of New York , Mr. Harder of California , Mr. Huffman , Ms. Jacobs , Ms. Kamlager-Dove , Mr. Khanna , Mr. Levin , Mr. Lieu , Ms. Matsui , Mrs. McIver , Mr. Moskowitz , Mr. Mullin , Mr. Neguse , Ms. Norton , Mr. Panetta , Ms. Pettersen , Mr. Ruiz , Ms. Schrier , Mr. Takano , Ms. Tlaib , Ms. Tokuda , Mrs. Torres of California , Mr. Vasquez , and Mr. Whitesides ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to require the President to establish an individual household disaster mitigation program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Resiliency and Coverage Act of 2025 .\n#### 2. Individual household disaster mitigation program\n##### (a) Establishment of program\nTitle II of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5131 et seq. ) is amended by adding at the end the following:\n207. Individual household disaster mitigation program (a) Establishment The President shall establish a program to provide grants to States and Indian tribal governments for qualifying pre-disaster mitigation activities on individual residential households that are at risk of being damaged by a major disaster. (b) Establishment of eligible disaster areas In carrying out the program under this section, the President shall\u2014 (1) establish eligible disaster areas, in consultation with States, that the President determines to be at risk of a natural hazard, including\u2014 (A) a description of the type, likelihood, and severity of each potential natural hazard affecting each such risk area; and (B) by taking into account previously declared major disasters impacting such areas; (2) provide technical assistance to the States or Indian tribal governments in developing the plan described in subsection (c) and administering grants provided for individual households under the program; (3) not less frequently than every 5 years, review and update the eligible disaster areas that the President determines to be at risk of a natural disaster, including a description of the type and severity of each potential natural disaster affecting each such risk area; and (4) consult with relevant governmental and nongovernmental experts in order to ensure that such determinations are made using current scientific standards and tools available in establishing, reviewing, and updating the eligible disaster areas that the President determines to be at risk of a natural disaster. (c) Plan for eligible activities To be eligible for a grant under this section, a State or Indian tribal government shall submit to the President a plan that includes\u2014 (1) each disaster risk area established by the President under subsection (b) in which the State or Indian tribal government proposes to provide funds under the program; (2) an assessment of the availability and affordability of homeowner insurance coverage in each such risk area, including a breakdown of coverage offered by\u2014 (A) private insurance companies; (B) State residual markets; and (C) State and Federal insurance programs; (3) an analysis of factors that may be adversely impacting insurance availability and affordability; (4) a list of each qualifying mitigation activity that is eligible for funds in each such risk area; (5) the criteria by which a State or Indian tribal government will evaluate applicants, which shall include consideration of the household income of the applicant and whether the residence is located in a Community Disaster Resilience Zone; and (6) a financial plan that includes maximum amounts available to a household for each qualifying mitigation activity. (d) Consultation In establishing the program under this section, the President, acting through the Administrator of the Federal Emergency Management Agency and the Director of the Federal Insurance Office, shall consult with the chief insurance regulators from the 50 States, the District of Columbia, and the territories of the United States, insurance industry stakeholders, including insurers, reinsurers, agents, brokers, and insurance-funded research organizations, and consumer and environmental stakeholders to determine what qualifying mitigation activities are likely to incentivize the availability and purchase of residential property insurance and other financial risk transfer mechanisms in eligible disaster areas. (e) Limitations (1) High-risk areas Funds provided under this section may only be used in eligible disaster areas that the State or Indian tribal government determines are at a high risk of experiencing a major disaster for the major disaster that presents such a risk. (2) Limitation based on adjusted gross income An individual shall not be eligible to receive a grant under this section if the adjusted gross income of such individual exceeds $250,000 ($500,000 in the case of a joint tax return) for the taxable year ending in the calendar year immediately preceding the calendar year with respect to which a grant application is filed. (3) Definition of adjusted gross income In this section, the term adjusted gross income has the meaning given such term in section 62(a) of the Internal Revenue Code of 1986. (f) Multi-Tiered mitigation standards (1) In general The President, acting through the Administrator of the Federal Emergency Management Agency, shall establish mitigation standards for individual households that carry out each type of qualifying mitigation activity eligible for funds under the program, which may include a multi-tiered standard. (2) Consideration In establishing the mitigation standards under paragraph (1), the President, acting through the Administrator\u2014 (A) shall consider any standards established by\u2014 (i) the Insurance Institute for Business and Home Safety; (ii) the chief insurance regulators from the 50 states, the District of Columbia, and the territories of the United States; and (iii) any other standard-issuing entity determined appropriate; and (B) may\u2014 (i) adopt a standard considered under subparagraph (A); or (ii) establish alternative standards. (g) Guidance to insurance providers To be eligible for a grant under the program under this section, a State or Indian tribal government shall establish, and make available to the public, guidance to insurance providers and consumers that includes suggested incentives for households that carry out disaster mitigation activities under the program, including\u2014 (1) the mitigation standards established under subsection (f); (2) increased consumer coverage choice; and (3) actuarially supported favorable pricing benefits such as discounts, rebates, or premium credits. (h) Maximum amounts A State or Indian tribal government may not provide more than an amount of $10,000, not to exceed the actual cost of mitigation activities, to any individual household under the program. Such amount shall be increased yearly to reflect any increase in the Consumer Price Index. (i) Definition of qualifying mitigation activity In this section, the term qualifying mitigation activity means an activity relating to a housing unit\u2014 (1) for property to\u2014 (A) improve the strength of a roof deck attachment; (B) create a secondary water barrier to prevent water intrusion or mitigate against potential water intrusion from wind-driven rain; (C) improve the durability, impact resistance (not less than class 3 or 4 rating), or fire resistance (not less than class A rating) of a roof covering; (D) brace gable-end walls; (E) reinforce the connection between a roof and supporting wall; (F) protect openings from penetration by wind-borne debris; (G) protect exterior doors and garages from natural hazards; (H) complete measures contained in the publication of the Federal Emergency Management Agency entitled Wind Retrofit Guide for Residential Buildings (P\u2013804); (I) elevate the qualified dwelling unit, as well as utilities, machinery, or equipment, above the base flood elevation or other applicable minimum elevation requirement; (J) seal walls in the basement of the qualified dwelling unit using waterproofing compounds; or (K) protect propane tanks or other external fuel sources; (2) to install\u2014 (A) check valves to prevent flood water from backing up into drains; (B) flood vents, breakaway walls or open lattice for homes located in V zones; (C) a stormwater drainage system or improve an existing system; (D) natural or nature-based features for flood control, including living shorelines; (E) roof coverings, sheathing, flashing, roof and attic vents, eaves, or gutters that conform to ignition-resistant construction standards; (F) wall components for wall assemblies that conform to ignition-resistant construction standards; (G) a wall-to-foundation anchor or connector, or a shear transfer anchor or connector; (H) wood structural panel sheathing for strengthening cripple walls; (I) anchorage of the masonry chimney to the framing; (J) prefabricated lateral resisting systems; (K) a standby generator system consisting of a standby generator and an automatic transfer switch; (L) a storm shelter that meets the design and construction standards established by the International Code Council and the National Storm Shelter Association (ICC\u2013500), or a safe room that satisfies the criteria contained in\u2014 (i) the publication of the Federal Emergency Management Agency entitled Safe Rooms for Tornadoes and Hurricanes (P\u2013361); or (ii) the publication of the Federal Emergency Management Agency entitled Taking Shelter from the Storm (P\u2013320); (M) a lightning protection system; (N) exterior walls, doors, windows, or other exterior dwelling unit elements that conform to ignition-resistant construction standards; (O) exterior deck or fence components that conform to ignition-resistant construction standards; (P) structure-specific water hydration systems, including fire mitigation systems such as interior sprinkler systems; (Q) flood openings for fully enclosed areas below the lowest floor of the dwelling unit; (R) lateral bracing for wall elements, foundation elements, and garage doors or other large openings to resist seismic loads; or (S) automatic shutoff valves for water and gas lines; (3) for services or equipment to\u2014 (A) create buffers around the qualified dwelling unit through the removal or reduction of flammable vegetation, including vertical clearance of tree branches; (B) create buffers around the dwelling unit through\u2014 (i) the removal of exterior deck or fence components or ignition-prone landscape features; or (ii) replacement of the components or features described in clause (i) with components or features that conform to ignition-resistant construction standards; (C) perform fire maintenance procedures identified by the Federal Emergency Management Agency or the United States Forest Service, including fuel management techniques such as creating fuel and fire breaks; or (D) replace flammable vegetation with less flammable species; (4) for property relating to satisfying the standards required for receipt of a FORTIFIED designation from the Insurance Institute for Business and Home Safety, provided that the qualified dwelling unit receives such designation following installation of such property; (5) for property relating to satisfying the standards required for receipt of a Wildfire Prepared Homes designation from the Insurance Institute for Business and Home Safety, provided that the qualified dwelling unit receives such designation following installation of such property; or (6) for any other hazard mitigation activity identified by the President, in consultation with the Administrator of the Federal Emergency Management Agency and the hazard mitigation advisory committee established in subsection (k), for mitigation of a natural hazard. (j) Hazard mitigation advisory committee The President shall establish a hazard mitigation advisory committee that shall\u2014 (1) consist of 50 representatives, including representatives from\u2014 (A) the State Insurance Commissioners; (B) private insurance companies; (C) private reinsurance companies; (D) insurance broker companies; (E) insurance-funded research organizations; (F) consumer advocate organizations; (G) State, local, and tribal firefighting agencies; (H) State-sponsored insurance plans; (I) realtor associations; (J) home builder associations; (K) State, local, and tribal emergency responders; (L) State and tribal emergency managers; (M) State and tribal hazard mitigation officers; (N) relevant academic experts; (O) building code associations; (P) agricultural groups; and (Q) environmental organizations; and (2) advise the President on developments in emerging hazard mitigation research and testing and recommend additions to the qualified hazard mitigation activities eligible under this program, including reviewing the effectiveness of hazard mitigation systems, products, and designations submitted to the advisory committee by private or nongovernmental companies or organizations. (k) Rules of construction Nothing in this Act shall\u2014 (1) require a State or any other entity to base the assessment of the status of the availability of homeowner insurance coverage required under subsection (c)(2) on data not already collected by that entity absent this requirement; and (2) be construed to preempt the State regulation of the business of insurance or require, by the Federal Government or any State government, any insurance provider to alter the underwriting, pricing, and distribution of insurance. .\n##### (b) Tax treatment of individual household disaster mitigation program\n**(1) In general**\nSection 139 of the Internal Revenue Code of 1986 is amended by redesignating subsection (h) as subsection (i) and by inserting after subsection (g) the following new subsection:\n(h) Individual household disaster mitigation program Gross income shall not include amounts received under section 207 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply to amounts received after the date of the enactment of this Act.\n#### 3. Exclusion of amounts received from State-based catastrophe loss mitigation programs\n##### (a) In general\nSection 139 of the Internal Revenue Code of 1986, as amended by the preceding provisions of this Act, is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) State-Based catastrophe loss mitigation programs (1) In general Gross income shall not include any amount received by an individual as a qualified catastrophe loss mitigation payment under a program established or administered by a State, or a political subdivision or instrumentality thereof, for the purpose of making such payments. (2) Qualified catastrophe loss mitigation payment For purposes of this section, the term qualified catastrophe loss mitigation payment means any amount which is received by an individual to make improvements to such individual\u2019s residence for the sole purpose of hazard mitigation with respect to such residence. (3) No increase in basis Rules similar to the rules of subsection (g)(3) shall apply in the case of this subsection. .\n##### (b) Conforming amendments\n**(1)**\nSection 139(d) is amended by striking and qualified and inserting , qualified catastrophe mitigation payments, and qualified .\n**(2)**\nSection 139(i) (as redesignated by subsection (a)) is amended by striking or qualified and inserting , qualified catastrophe mitigation payment, or qualified .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 4. Exclusion from gross income of certain emergency agricultural assistance\n##### (a) In general\nSection 139 of the Internal Revenue Code of 1986, as amended by the preceding provisions of this Act, is amended by redesignating subsection (j) as subsection (k) and by inserting after subsection (i) the following new subsection:\n(j) Certain agricultural assistance For purposes of this section, the term qualified disaster relief payment shall include any assistance received under any of the following: (1) Assistance received under the Wildfires and Hurricanes Indemnity Program Plus under subpart O of part 760 of title 7, Code of Federal Regulations. (2) Assistance received under section 1501 of the Agricultural Act of 2014 ( 7 U.S.C. 9081 ). (3) Noninsured crop assistance under section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ). (4) Assistance under a food assistance program under part 9 of title 7, Code of Federal Regulations. (5) Assistance under title IV of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2201 et seq. ). (6) Assistance under the Quality Loss Assistance Program. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 5. Credit for disaster mitigation expenditures\n##### (a) In general\nSubpart B of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 27 the following new section:\n28. Disaster mitigation expenditures (a) In general There shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to 30 percent of the expenditures paid for qualifying mitigation activities paid or incurred by the taxpayer during such taxable year with respect to real property owned or leased by the taxpayer. (b) Qualified disaster mitigation activities For purposes of this section\u2014 (1) Qualifying mitigation activity The term qualifying mitigation activity has the meaning given such term in section 207(j) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act. (2) Treatment of reimbursements Any amount originally paid or incurred by the taxpayer which is reimbursed by a State under a qualified State disaster mitigation program shall be treated as paid by such State (and not by such taxpayer). (c) Application with other credits (1) Business credit treated as part of general business credit So much of the credit which would be allowed under subsection (a) for any taxable year (determined without regard to this subsection) that is attributable to expenditures made in the ordinary course of the taxpayer\u2019s trade or business (or, in the case of expenditures made by a State, would have been expenditures made in the ordinary course of the taxpayer\u2019s trade or business if made by the taxpayer) shall be treated as a credit listed in section 38(b) for taxable year (and not allowed under subsection (a)). (2) Personal credit For purposes of this title, the credit allowed under subsection (a) for any taxable year (determined after application of paragraph (1)) shall be treated as a credit allowable under subpart A for such taxable year. (d) Reduction of credit percentage where taxpayer expenditures less than 30 percent (1) In general If the expenditure percentage with respect to any item of expenditure described under subsection (a) is less than 30 percent, subsection (a) shall be applied by substituting the expenditure percentage for 30 percent with respect to such item of expenditure. (2) Expenditure percentage For purposes of this section, the term expenditure percentage means, with respect to any item of expenditure described under subsection (a) any portion of which is paid or incurred by a State, the ratio (expressed as a percentage) of\u2014 (A) the taxpayer\u2019s expenditure for such item, divided by (B) the sum of the taxpayer\u2019s and such State\u2019s expenditures for such item. (e) Special rules (1) Treatment of expenditures related to marketable timber An expenditure shall not be taken into account for purposes of this section (whether made by the taxpayer or a State) if such expenditure is properly allocable to timber which is sold or exchanged by the taxpayer. The preceding sentence shall not apply to the extent that such amount exceeds the gain on such sale or exchange. (2) Basis reduction For purposes of this subtitle, if the basis of any property would (but for this paragraph) be determined by taking into account any expenditure described under subsection (a), the basis of such property shall be reduced by the amount of the credit allowed under subsection (a) with respect to such expenditure (determined without regard to subsection (c)). (3) Denial of double benefit The amount of any deduction or other credit allowable under this chapter for any expenditure for which a credit is allowable under subsection (a) shall be reduced by the amount of credit allowed under such subsection for such expenditure (determined without regard to subsection (c)). .\n##### (b) Conforming amendments\n**(1)**\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the portion of the disaster mitigation expenditures credit to which section 28(c)(1) applies. .\n**(2)**\nSection 1016(a) of such Code is amended by redesignating paragraphs (35) through (38) as paragraphs (36) through (39), respectively, and by inserting after paragraph (34) the following new paragraph:\n(35) to the extent provided in section 28(e)(2), .\n**(3)**\nThe table of sections for subpart B of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 27 the following new item:\nSec. 28. Qualified disaster mitigation expenditures. .\n##### (c) Effective date\nThe amendments made by this section shall apply to expenditures paid or incurred after the date of the enactment of this Act, in taxable years ending after such date.",
      "versionDate": "2025-02-06",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Emergency Management",
        "updateDate": "2025-05-05T15:57:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119hr1105",
          "measure-number": "1105",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2026-05-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1105v00",
            "update-date": "2026-05-11"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disaster Resiliency and Coverage Act of 2025</strong></p><p>This bill establishes a grant program for certain hazard mitigation measures for homes in disaster risk areas and provides a tax credit for up to 30% of expenditures on such mitigation measures. It also excludes from taxable income certain payments for residential hazard mitigation and federal emergency agricultural assistance.\u00a0</p><p>The bill requires the Federal Emergency Management Agency (FEMA) to award grants to states and Indian tribal governments for specified hazard mitigation activities on residential properties at a high risk of experiencing a major disaster. FEMA must establish and periodically update disaster risk areas in which homes are eligible for the grant funding. Individual residential households, subject to certain income limitations, may receive up to $10,000 (adjusted for inflation) for eligible hazard mitigation activities, such as reinforcing a roof, installing a flood control system, or reducing flammable vegetation near the home. The bill also provides an income tax credit to individuals and businesses for up to 30% of expenditures on the specified residential mitigation activities eligible under the grant program.</p><p>Additionally, under current law, payments for disaster relief and payments under federal hazard mitigation programs are excluded from taxable income. The bill specifically excludes from taxable income payments to an individual for hazard mitigation improvements to their residence under any program established or administered by a state or local government. The bill also excludes certain federal emergency and disaster agricultural assistance from taxable income as a type of disaster relief payment.</p>"
        },
        "title": "Disaster Resiliency and Coverage Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1105.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Resiliency and Coverage Act of 2025</strong></p><p>This bill establishes a grant program for certain hazard mitigation measures for homes in disaster risk areas and provides a tax credit for up to 30% of expenditures on such mitigation measures. It also excludes from taxable income certain payments for residential hazard mitigation and federal emergency agricultural assistance.\u00a0</p><p>The bill requires the Federal Emergency Management Agency (FEMA) to award grants to states and Indian tribal governments for specified hazard mitigation activities on residential properties at a high risk of experiencing a major disaster. FEMA must establish and periodically update disaster risk areas in which homes are eligible for the grant funding. Individual residential households, subject to certain income limitations, may receive up to $10,000 (adjusted for inflation) for eligible hazard mitigation activities, such as reinforcing a roof, installing a flood control system, or reducing flammable vegetation near the home. The bill also provides an income tax credit to individuals and businesses for up to 30% of expenditures on the specified residential mitigation activities eligible under the grant program.</p><p>Additionally, under current law, payments for disaster relief and payments under federal hazard mitigation programs are excluded from taxable income. The bill specifically excludes from taxable income payments to an individual for hazard mitigation improvements to their residence under any program established or administered by a state or local government. The bill also excludes certain federal emergency and disaster agricultural assistance from taxable income as a type of disaster relief payment.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr1105"
    },
    "title": "Disaster Resiliency and Coverage Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Resiliency and Coverage Act of 2025</strong></p><p>This bill establishes a grant program for certain hazard mitigation measures for homes in disaster risk areas and provides a tax credit for up to 30% of expenditures on such mitigation measures. It also excludes from taxable income certain payments for residential hazard mitigation and federal emergency agricultural assistance.\u00a0</p><p>The bill requires the Federal Emergency Management Agency (FEMA) to award grants to states and Indian tribal governments for specified hazard mitigation activities on residential properties at a high risk of experiencing a major disaster. FEMA must establish and periodically update disaster risk areas in which homes are eligible for the grant funding. Individual residential households, subject to certain income limitations, may receive up to $10,000 (adjusted for inflation) for eligible hazard mitigation activities, such as reinforcing a roof, installing a flood control system, or reducing flammable vegetation near the home. The bill also provides an income tax credit to individuals and businesses for up to 30% of expenditures on the specified residential mitigation activities eligible under the grant program.</p><p>Additionally, under current law, payments for disaster relief and payments under federal hazard mitigation programs are excluded from taxable income. The bill specifically excludes from taxable income payments to an individual for hazard mitigation improvements to their residence under any program established or administered by a state or local government. The bill also excludes certain federal emergency and disaster agricultural assistance from taxable income as a type of disaster relief payment.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr1105"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1105ih.xml"
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
      "title": "Disaster Resiliency and Coverage Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Resiliency and Coverage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to require the President to establish an individual household disaster mitigation program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T05:18:30Z"
    }
  ]
}
```
