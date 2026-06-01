# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5390?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5390
- Title: FAMILY Act
- Congress: 119
- Bill type: HR
- Bill number: 5390
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2026-05-14T08:08:38Z
- Update date including text: 2026-05-14T08:08:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5390",
    "number": "5390",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "FAMILY Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:38Z",
    "updateDateIncludingText": "2026-05-14T08:08:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:04:05Z",
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
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "AL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "AL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "A000371",
      "district": "33",
      "firstName": "Pete",
      "fullName": "Rep. Aguilar, Pete [D-CA-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Aguilar",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
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
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
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
      "sponsorshipDate": "2025-09-16",
      "state": "DC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "DE"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "HI"
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
      "sponsorshipDate": "2025-09-16",
      "state": "HI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-16",
      "state": "IN"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IN"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "KY"
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
      "sponsorshipDate": "2025-09-16",
      "state": "LA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "LA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
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
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "ME"
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
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
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
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MO"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MO"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MS"
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
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NH"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
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
      "sponsorshipDate": "2025-09-16",
      "state": "NM"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NM"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NV"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NV"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OH"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OH"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OH"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OH"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OH"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PR"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "RI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "RI"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "SC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TN"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VI"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VT"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WI"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WI"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
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
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NM"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "TX"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "WA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NV"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NH"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
    },
    {
      "bioguideId": "M001245",
      "district": "18",
      "firstName": "Christian",
      "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Menefee",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "M001246",
      "district": "11",
      "firstName": "Analilia",
      "fullName": "Rep. Mejia, Analilia [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Mejia",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NJ"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5390ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5390\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Ms. DeLauro (for herself, Mr. Figures , Ms. Sewell , Ms. Ansari , Mr. Huffman , Mr. Thompson of California , Mr. Bera , Ms. Matsui , Mr. Garamendi , Mr. DeSaulnier , Ms. Pelosi , Ms. Simon , Mr. Swalwell , Mr. Mullin , Mr. Khanna , Ms. Lofgren , Mr. Panetta , Mr. Costa , Mr. Carbajal , Mr. Ruiz , Ms. Brownley , Mr. Whitesides , Ms. Chu , Ms. Rivas , Ms. Friedman , Mr. Cisneros , Mr. Sherman , Mr. Aguilar , Mr. Gomez , Mrs. Torres of California , Mr. Lieu , Ms. Kamlager-Dove , Ms. S\u00e1nchez , Mr. Takano , Mr. Garcia of California , Ms. Waters , Ms. Barrag\u00e1n , Mr. Tran , Mr. Min , Mr. Levin , Ms. Jacobs , Mr. Vargas , Ms. DeGette , Mr. Neguse , Mr. Crow , Ms. Pettersen , Mr. Larson of Connecticut , Mr. Courtney , Mr. Himes , Mrs. Hayes , Ms. Norton , Ms. McBride , Mr. Soto , Mr. Frost , Ms. Castor of Florida , Mrs. Cherfilus-McCormick , Ms. Lois Frankel of Florida , Mr. Moskowitz , Ms. Wilson of Florida , Ms. Wasserman Schultz , Mr. Bishop , Mr. Johnson of Georgia , Ms. Williams of Georgia , Mrs. McBath , Mr. David Scott of Georgia , Mr. Case , Ms. Tokuda , Mr. Jackson of Illinois , Ms. Kelly of Illinois , Mrs. Ramirez , Mr. Garc\u00eda of Illinois , Mr. Quigley , Mr. Casten , Mr. Davis of Illinois , Mr. Krishnamoorthi , Ms. Schakowsky , Mr. Schneider , Mr. Foster , Ms. Budzinski , Ms. Underwood , Mr. Sorensen , Mr. Mrvan , Mr. Carson , Mr. McGarvey , Mr. Carter of Louisiana , Mr. Fields , Mr. McGovern , Mrs. Trahan , Mr. Moulton , Ms. Pressley , Mr. Lynch , Mr. Keating , Mr. Olszewski , Ms. Elfreth , Mr. Ivey , Mr. Hoyer , Mrs. McClain Delaney , Mr. Mfume , Mr. Raskin , Ms. Pingree , Ms. Scholten , Mrs. Dingell , Ms. McDonald Rivet , Ms. Stevens , Ms. Tlaib , Mr. Thanedar , Ms. Craig , Ms. Morrison , Ms. McCollum , Ms. Omar , Mr. Bell , Mr. Cleaver , Mr. Thompson of Mississippi , Ms. Ross , Mrs. Foushee , Ms. Adams , Ms. Goodlander , Mr. Norcross , Mr. Conaway , Mr. Gottheimer , Mr. Pallone , Mr. Menendez , Mrs. McIver , Ms. Sherrill , Mrs. Watson Coleman , Ms. Stansbury , Ms. Leger Fernandez , Ms. Titus , Mr. Horsford , Ms. Meng , Ms. Vel\u00e1zquez , Ms. Clarke of New York , Mr. Goldman of New York , Mr. Nadler , Mr. Espaillat , Ms. Ocasio-Cortez , Mr. Torres of New York , Mr. Latimer , Mr. Riley of New York , Mr. Tonko , Mr. Mannion , Mr. Morelle , Mr. Kennedy of New York , Mr. Landsman , Mrs. Beatty , Ms. Kaptur , Ms. Brown , Mrs. Sykes , Ms. Bonamici , Ms. Dexter , Ms. Hoyle of Oregon , Ms. Bynum , Ms. Salinas , Mr. Boyle of Pennsylvania , Mr. Evans of Pennsylvania , Ms. Dean of Pennsylvania , Ms. Scanlon , Ms. Houlahan , Ms. Lee of Pennsylvania , Mr. Deluzio , Mr. Hern\u00e1ndez , Mr. Amo , Mr. Magaziner , Mr. Clyburn , Mr. Cohen , Mrs. Fletcher , Mr. Green of Texas , Ms. Escobar , Mr. Castro of Texas , Ms. Garcia of Texas , Ms. Crockett , Ms. Johnson of Texas , Mr. Veasey , Mr. Vicente Gonzalez of Texas , Mr. Casar , Mr. Doggett , Ms. McClellan , Mr. Beyer , Mr. Subramanyam , Mr. Walkinshaw , Ms. Plaskett , Ms. Balint , Ms. DelBene , Mr. Larsen of Washington , Ms. Randall , Ms. Jayapal , Mr. Smith of Washington , Ms. Strickland , Mr. Pocan , Ms. Moore of Wisconsin , and Mr. Liccardo ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide paid family and medical leave benefits to certain individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Family and Medical Insurance Leave Act or the FAMILY Act .\n#### 2. Definitions\nIn this Act:\n**(1) Caregiving hour**\n**(A) In general**\nThe term caregiving hour means, with respect to an individual, a 1-hour period during which the individual engaged in qualified caregiving.\n**(B) Limitations**\nAn individual may not exceed with respect to any benefit period, a number of caregiving hours equal to 12 times the number of hours in a regular workweek of the individual (as determined under subparagraph (C)).\n**(C) Number of hours in a regular workweek**\nFor purposes of this Act, the number of hours in a regular workweek of an individual shall be the number of hours that the individual regularly works in a week for all employers or as a self-employed individual (or regularly worked in the case of an individual who is no longer working or whose total weekly hours of work have been reduced) during the month before the individual\u2019s benefit period begins (or prior to such month, if applicable in the case of an individual who is no longer working or whose total weekly hours of work have been reduced).\n**(2) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(3) Deputy Commissioner**\nThe term Deputy Commissioner means the Deputy Commissioner who heads the Office of Paid Family and Medical Leave established under section 3(a).\n**(4) Eligible individual**\nThe term eligible individual means an individual who is entitled to a benefit under section 4 for a particular month, upon filing an application for such benefit for such month.\n**(5) National average wage index**\nThe term national average wage index has the meaning given such term in section 209(k)(1) of the Social Security Act ( 42 U.S.C. 409(k)(1) ).\n**(6) Qualified caregiving**\n**(A) In general**\nThe term qualified caregiving means any activity engaged in by an individual, other than regular employment, for a qualifying reason.\n**(B) Qualifying reason**\n**(i) In general**\nFor purposes of subparagraph (A), the term qualifying reason means any of the following reasons for taking leave:\n**(I)**\nAny reason for which an eligible employee would be entitled to leave under subparagraph (A), (B), or (E) of paragraph (1) of section 102(a) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a) ).\n**(II)**\nIn order to care for a qualified family member of the individual, if such qualified family member has a serious health condition.\n**(III)**\nBecause of a serious health condition that makes the individual unable to perform the services required under the terms of their regular employment.\n**(IV)**\nBecause the individual, or a qualified family member, is a victim of a qualifying act of violence, if the leave is for the individual to do any of the following or to assist the individual\u2019s qualified family member to, as a result of such violence, do any of the following:\n**(aa)**\nSeek, receive, or secure counseling.\n**(bb)**\nSeek or secure temporary or permanent relocation or take steps to secure an existing home.\n**(cc)**\nSeek, receive, or follow up on assistance from a victim services organization or agency providing services to victims.\n**(dd)**\nSeek legal assistance or attend legal proceedings, including preparation for or participation in any related administrative, civil, or criminal legal proceedings or other related activities.\n**(ee)**\nSeek medical attention for physical or psychological injury or disability caused or aggravated by the qualifying act of violence.\n**(ff)**\nEnroll in a new school or care arrangement.\n**(gg)**\nTake other steps necessary to protect or restore their physical, mental, emotional, spiritual, and economic well-being or the well-being of a qualified family member recovering from a qualifying act of violence.\n**(ii) Qualified family member; serious health condition**\nIn this subparagraph:\n**(I) Qualified family member**\nThe term qualified family member means, with respect to an individual\u2014\n**(aa)**\na spouse (including a domestic partner in a civil union or other registered domestic partnership recognized by a State) or a parent of such spouse;\n**(bb)**\na child (regardless of age) or a child\u2019s spouse;\n**(cc)**\na parent or a parent\u2019s spouse;\n**(dd)**\na sibling or a sibling\u2019s spouse;\n**(ee)**\na grandparent, a grandchild, or a spouse of a grandparent or grandchild; and\n**(ff)**\nany other individual who is related by blood or affinity and whose association with the employee is equivalent of a family relationship.\n**(II) Serious health condition**\nThe term serious health condition has the meaning given such term in section 101(11) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(11) ).\n**(iii) Treatment of individuals covered by legacy State comprehensive paid leave program**\n**(I) In general**\nFor purposes of subparagraph (A), an activity engaged in by an individual shall not be considered as other than regular employment if, for the time during which the individual was so engaged, the individual is taking leave from covered employment under the law of a legacy State (as defined in section 4(c)).\n**(II) Unemployed**\nIn the case of an individual who is no longer employed, such individual shall be treated, for purposes of clause (i), as taking leave from covered employment under the law of a legacy State (as so defined) with respect to the portion of the time during which the individual was engaged in an activity for a qualifying reason corresponding to the share of the individual\u2019s workweek that was in covered employment under the law of a legacy State (as so defined).\n**(C) Other definitions**\nFor purposes of this paragraph:\n**(i) Child**\nThe term child means, regardless of age, a biological, foster, or adopted child, a stepchild, a child of a domestic partner, a legal ward, or a child of a person standing in loco parentis.\n**(ii) Domestic partner**\n**(I) In general**\nThe term domestic partner , with respect to an individual, means another individual with whom the individual is in a committed relationship.\n**(II) Committed relationship defined**\nThe term committed relationship means a relationship between 2 individuals, each at least 18 years of age, in which each individual is the other individual\u2019s sole domestic partner and both individuals share responsibility for a significant measure of each other\u2019s common welfare. The term includes any such relationship between 2 individuals, including individuals of the same sex, that is granted legal recognition by a State or political subdivision of a State as a marriage or analogous relationship, including a civil union or domestic partnership.\n**(iii) Dating violence**\nThe term dating violence has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(iv) Domestic violence**\nThe term domestic violence has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ), except that the reference in such section to the term jurisdiction receiving grant funding shall be deemed to mean the jurisdiction in which the victim lives or the jurisdiction in which the employer involved is located.\n**(v) Parent**\nThe term parent means a biological, foster, or adoptive parent of an employee, a stepparent of an employee, parent-in-law, parent of a domestic partner, or a legal guardian or other person who stood in loco parentis to an employee when the employee was a child.\n**(vi) Qualifying act of violence**\nThe term qualifying act of violence means an act, conduct, or pattern of conduct that could constitute any of the following:\n**(I)**\ndating violence;\n**(II)**\ndomestic violence;\n**(III)**\nfamily violence;\n**(IV)**\nsexual assault;\n**(V)**\nsex trafficking;\n**(VI)**\nstalking;\n**(VII)**\nother forms of gender based violence or harassment; or\n**(VIII)**\nan act, conduct, or pattern of conduct\u2014\n**(aa)**\nin which an individual causes or threatens to cause bodily injury or death to another individual;\n**(bb)**\nin which an individual exhibits, draws, brandishes, or uses a firearm, or other dangerous weapon, with respect to another individual; or\n**(cc)**\nin which an individual uses, or makes a reasonably perceived or actual threat to use, force against another individual to cause bodily injury or death.\n**(vii) Sexual assault**\nThe term sexual assault has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(viii) Sex trafficking**\nThe term sex trafficking has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(ix) Spouse**\nThe term spouse , with respect to an employee, has the meaning given such term by the marriage laws of the State in which the marriage was celebrated.\n**(x) Stalking**\nThe term stalking has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(xi) Victim services organization**\nThe term victim services organization means a nonprofit, nongovernmental organization that provides assistance to victims of a qualifying act of violence or advocates for such victims, including a rape crisis center, an organization carrying out a qualifying act of violence prevention or treatment program, an organization operating a shelter or providing counseling services, or a legal services organization or other organization providing assistance through the legal process.\n**(7) Self-employment income**\nThe term self-employment income has the same meaning as such term in section 211(b) of such Act ( 42 U.S.C. 411(b) ).\n**(8) State**\nThe term State means any State of the United States or the District of Columbia or any territory or possession of the United States.\n**(9) Wages**\nThe term wages has the meaning given such term in section 3121(a) of the Internal Revenue Code of 1986 for purposes of the taxes imposed by sections 3101(b) and 3111(b) of such Code (without regard to section 3121(u)(2)(C) of such Code), except that such term also includes\u2014\n**(A)**\ncompensation, as defined in section 3231(e) of such Code for purposes of the Railroad Retirement Tax Act; and\n**(B)**\nunemployment compensation, as defined in section 85(b) of such Code.\n#### 3. Office of Paid Family and Medical Leave\n##### (a) Establishment of Office\nThere is established within the Social Security Administration an office to be known as the Office of Paid Family and Medical Leave. The Office shall be headed by a Deputy Commissioner who shall be appointed by the Commissioner.\n##### (b) Responsibilities of Deputy Commissioner\nThe Commissioner, acting through the Deputy Commissioner, shall be responsible for\u2014\n**(1)**\nhiring personnel and making employment decisions with regard to such personnel;\n**(2)**\nissuing such regulations as may be necessary to carry out the purposes of this Act;\n**(3)**\nentering into cooperative agreements with other agencies and departments to ensure the efficiency of the administration of the program;\n**(4)**\ndetermining eligibility for family and medical leave insurance benefits under section 4;\n**(5)**\ndetermining benefit amounts for each month of such eligibility and making timely payments of such benefits to entitled individuals in accordance with such section;\n**(6)**\nestablishing and maintaining a system of records relating to the administration of such section;\n**(7)**\npreventing fraud and abuse relating to such benefits;\n**(8)**\nproviding information on request regarding eligibility requirements, the claims process, benefit amounts, maximum benefits payable, notice requirements, nondiscrimination rights, confidentiality, coordination of leave under this Act and other laws, collective bargaining agreements, and employer policies;\n**(9)**\nannually providing employers a notice to inform employees of the availability of such benefits;\n**(10)**\nannually making available to the public a report that includes the number of individuals who received such benefits, the purposes for which such benefits were received, and an analysis of utilization rates of such benefits by gender, race, ethnicity, and income levels; and\n**(11)**\ntailoring culturally and linguistically competent education and outreach toward increasing utilization rates of benefits under such section.\n##### (c) Availability of data\nNotwithstanding any other provision of law, the Commissioner shall make available to the Deputy Commissioner such data as the Commissioner determines necessary to enable the Deputy Commissioner to effectively carry out the responsibilities described in subsection (b).\n##### (d) Datasharing\nThe Commissioner and the heads of Federal agencies shall make good faith efforts to enter into datasharing agreements to enable the Deputy Commissioner to effectively carry out the responsibilities described in subsection (b).\n##### (e) Report to Congress\nNot later than 12 months after the date of enactment of this Act, the Commissioner shall submit to Congress a report including information on the following:\n**(1)**\nDatabases maintained by Federal agencies that contain information necessary to carry out the purposes of this Act, including information on any congressional action needed to permit the Commissioner to access such databases for such purposes.\n**(2)**\nThe feasibility of expediting the review of applications under paragraph (1) of section 4(f) and the payment of monthly benefit payments under paragraph (2) of such section, including the effects of establishing shorter time frames for such reviews and payment in statute.\n#### 4. Family and Medical Leave Insurance benefit payments\n##### (a) In general\n**(1) Requirements**\nEvery individual who\u2014\n**(A)**\nhas filed an application for a family and medical leave insurance benefit in accordance with subsection (d);\n**(B)**\nwas engaged in qualified caregiving, or anticipates being so engaged, during the period that begins 90 days before the date on which such application is filed and ends 30 days after such date;\n**(C)**\nhas wages or self-employment income at any time during the period\u2014\n**(i)**\nbeginning with the most recent calendar quarter that ends at least 4 months prior to the beginning of the individual\u2019s benefit period specified in subsection (c); and\n**(ii)**\nending with the month before the month in which such benefit period begins; and\n**(D)**\nhas at least the specified amount of wages and self-employment income during the most recent 8-calendar quarter period that ends at least 4 months prior to the beginning of the individual\u2019s benefit period specified in subsection (c),\nshall be entitled to such a benefit for each month in such benefit period.\n**(2) Specified amount**\nFor purposes of paragraph (1)(D), the specified amount shall be\u2014\n**(A)**\nif the benefit period begins in calendar year 2026, $2,000; and\n**(B)**\nif the benefit period begins in any calendar year after 2026, an amount equal to the greater of\u2014\n**(i)**\nthe specified amount applicable for the preceding calendar year; or\n**(ii)**\nan amount equal to the product of\u2014\n**(I)**\n$2,000; multiplied by\n**(II)**\nan amount equal to the quotient of\u2014\n**(aa)**\nthe national average wage index for the second calendar year preceding such calendar year; divided by\n**(bb)**\nthe national average wage index for 2024.\n##### (b) Benefit amount\n**(1) In general**\nExcept as otherwise provided in this subsection, the benefit amount to which an individual is entitled under this section for a month shall be an amount equal to the product of\u2014\n**(A)**\nthe greater of\u2014\n**(i)**\nthe lesser of\u2014\n**(I)**\nan amount equal to the monthly benefit rate determined under paragraph (2); and\n**(II)**\nthe maximum benefit amount determined under paragraph (3); and\n**(ii)**\nthe minimum benefit amount determined under paragraph (3); and\n**(B)**\nthe quotient (not greater than 1) obtained by dividing the number of caregiving hours of the individual in such month by the product of\u2014\n**(i)**\nthe number of hours in a regular workweek of the individuals; and\n**(ii)**\nthe number of workweeks (including partial workweeks) in such month.\n**(2) Monthly benefit rate**\n**(A) In general**\nFor purposes of this subsection, the monthly benefit rate of an individual shall be an amount equal to the sum of\u2014\n**(i)**\n85 percent of the individual\u2019s average monthly earnings to the extent that such earnings do not exceed the amount established for purposes of this clause by subparagraph (B);\n**(ii)**\n69 percent of the individual\u2019s average monthly earnings to the extent that such earnings exceed the amount established for purposes of clause (i) but do not exceed the amount established for purposes of this clause by subparagraph (B); and\n**(iii)**\n50 percent of the individual\u2019s average monthly earnings to the extent that such earnings exceed the amount established for purposes of clause (ii) but do not exceed the amount established for purposes of this clause by subparagraph (B).\n**(B) Amounts established**\n**(i) Initial amounts**\nFor individuals whose benefit period begins in calendar year 2026, the amount established for purposes of clauses (i), (ii), and (iii) of subparagraph (A) shall be $1,257, $3,500, and $6,200, respectively.\n**(ii) Wage indexing**\nFor individuals whose benefit period begins in any calendar year after 2026, each of the amounts so established shall equal the corresponding amount established for the calendar year preceding such calendar year, or, if larger, the product of the corresponding amount established with respect to the calendar year 2026 and the quotient obtained by dividing\u2014\n**(I)**\nthe national average wage index for the second calendar year preceding such calendar year, by\n**(II)**\nthe national average wage index for calendar year 2024.\n**(iii) Rounding**\nEach amount established under clause (ii) for any calendar year shall be rounded to the nearest $1, except that any amount so established which is a multiple of $0.50 but not of $1 shall be rounded to the next higher $1.\n**(C) Average monthly earnings**\nFor purposes of this subsection, the average monthly earnings of an individual shall be an amount equal to 1/12 of the wages and self-employment income of the individual for the calendar year in which such wages and self-employment income are the highest among the most recent 3 calendar years.\n**(3) Maximum and minimum benefit amounts**\n**(A) In general**\nFor individuals who initially become eligible for family and medical leave insurance benefits in the first full calendar year after the date of enactment of this Act, the maximum monthly benefit amount and the minimum monthly benefit amount shall be $4,000 and $580, respectively.\n**(B) Wage indexing**\nFor individuals who initially become eligible for family and medical leave insurance benefits in any calendar year after such first full calendar year the maximum benefit amount and the minimum benefit amount shall be, respectively, the product of the corresponding amount determined with respect to the first calendar year under subparagraph (A) and the quotient obtained by dividing\u2014\n**(i)**\nthe national average wage index for the second calendar year preceding the calendar year for which the determination is made, by\n**(ii)**\nthe national average wage index for the second calendar year preceding the first full calendar year after the date of enactment of this Act.\n**(4) Minimum caregiving hours**\nIn a case in which the number of caregiving hours of an individual for a month is less than 4, the individual shall be deemed to have zero caregiving hours for such month.\n**(5) Reduction in benefit amount on account of receipt of certain benefits**\nA benefit under this section for a month shall be reduced by the amount, if any, in certain benefits (as determined under regulations issued by the Commissioner) as may be otherwise received by an individual. For purposes of the preceding sentence, certain benefits include\u2014\n**(A)**\nperiodic benefits on account of such individual\u2019s total or partial disability under a workmen\u2019s compensation law or plan of the United States or a State; and\n**(B)**\nperiodic benefits on account of an individual\u2019s employment status under an unemployment law or plan of the United States or a State.\n##### (c) Benefit period\n**(1) In general**\nExcept as provided in paragraph (2), the benefit period specified in this subsection is the 12-month period that begins on the 1st day of the 1st month in which the individual\u2014\n**(A)**\nmeets the criteria specified in subparagraphs (A) and (B) of subsection (a)(1); and\n**(B)**\nwould meet the criteria specified in subparagraphs (C) and (D) of such subsection if such subparagraphs were applied by substituting such 12-month period for each reference to the individual's benefit period.\n**(2) Retroactive benefits**\nIn the case of an application for benefits under this section for qualified caregiving in which the individual was engaged at any time during the 90-day period preceding the date on which such application is submitted, the benefit period specified in this subsection shall begin on the later of\u2014\n**(A)**\nthe 1st day of the 1st month in which the individual engaged in such qualified caregiving; or\n**(B)**\nthe 1st day of the 1st month that begins during such 90-day period,\nand shall end on the date that is 365 days after the 1st day of the benefit period.\n##### (d) Application\nAn application for a family and medical leave insurance benefit shall include\u2014\n**(1)**\na statement that the individual was engaged in qualified caregiving, or anticipates being so engaged, during the period that begins 90 days before the date on which the application is submitted or within 30 days after such date;\n**(2)**\nif the qualified caregiving described in the statement in paragraph (1) is engaged in by the individual because of a serious health condition (as defined in subclause (II) of section 2(5)(B)(ii)) of the individual or a qualified family member (as defined in subclause (I) of such section) of the individual, a certification, issued by the health care provider treating such serious health condition, that affirms the information specified in paragraph (1) and contains such information as the Commissioner shall specify in regulations, which shall be no more than the information that is required to be stated under section 103(b) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2613(b) );\n**(3)**\nif such qualified caregiving is engaged in by the individual for any other qualifying reason (as defined in section 2(5)(B)(i)), a certification, issued by a relevant authority determined under regulations issued by the Commissioner, that affirms the circumstances giving rise to such reason; and\n**(4)**\nan attestation from the applicant that his or her employer has been provided with written notice of the individual\u2019s intention to take family or medical leave, if the individual has an employer, or to the Commissioner in all other cases.\n##### (e) Ineligibility; disqualification\n**(1) Ineligibility for benefit**\nAn individual shall be ineligible for a benefit under this section for any month for which the individual is entitled to\u2014\n**(A)**\ndisability insurance benefits under section 223 of the Social Security Act ( 42 U.S.C. 423 ) or a similar permanent disability program under any law or plan of a State or political subdivision or instrumentality of a State (as such terms are used in section 218 of the Social Security Act ( 42 U.S.C. 418 ));\n**(B)**\nmonthly insurance benefits under section 202 of such Act ( 42 U.S.C. 402 ) based on such individual's disability (as defined in section 223(d) of such Act ( 42 U.S.C. 423(d) )); or\n**(C)**\nbenefits under title XVI of such Act ( 42 U.S.C. 1381 et seq. ) based on such individual\u2019s status as a disabled individual (as determined under section 1614 of such Act ( 42 U.S.C. 1382c )).\n**(2) Disqualification**\nAn individual who has been convicted of a violation under section 208 of the Social Security Act ( 42 U.S.C. 408 ) or who has been found to have used false statements to secure benefits under this section, shall be ineligible for benefits under this section for a 1-year period following the date of such conviction.\n##### (f) Review of eligibility and benefit payment determinations\n**(1) Eligibility determinations**\n**(A) In general**\nThe Commissioner shall provide notice to an individual applying for benefits under this section of the initial determination of eligibility for such benefits, and the estimated benefit amount for a month in which four caregiving hours of the individual occur, as soon as practicable after the application is received.\n**(B) Review**\nAn individual may request review of an initial adverse determination with respect to such application at any time before the end of the 20-day period that begins on the date notice of such determination is received, except that such 20-day period may be extended for good cause. As soon as practicable after the individual requests review of the determination, the Commissioner shall provide notice to the individual of a final determination of eligibility for benefits under this section.\n**(2) Benefit payment determinations**\n**(A) In general**\nThe Commissioner shall make any monthly benefit payment to an individual claiming benefits for a month under this section, or provide notice of the reason such payment will not be made if the Commissioner determines that the individual is not entitled to payment for such month, not later than 20 days after the individual\u2019s monthly benefit claim report for such month is received. Such monthly report shall be filed with the Commissioner not later than 15 days after the end of each month.\n**(B) Review**\nIf the Commissioner determines that payment will not be made to an individual for a month, or if the Commissioner determines that payment shall be made based on a number of caregiving hours in the month inconsistent with the number of caregiving hours in the monthly benefit claim report of the individual for such month, the individual may request review of such determination at any time before the end of the 20-day period that begins on the date notice of such determination is received, except that such 20-day period may be extended for good cause. Not later than 20 days after the individual requests review of the determination, the Commissioner shall provide notice to the individual of a final determination of payment for such month, and shall make payment to the individual of any additional amount not included in the initial payment to the individual for such month to which the Commissioner determines the individual is entitled.\n**(3) Burden of proof**\nAn application for benefits under this section and a monthly benefit claim report of an individual shall each be presumed to be true and accurate, unless the Commissioner demonstrates by a preponderance of the evidence that information contained in the application is false.\n**(4) Definition of monthly benefit claim report**\nFor purposes of this subsection, the term monthly benefit claim report means, with respect to an individual for a month, the individual\u2019s report to the Commissioner of the number of caregiving hours of the individual in such month, which shall be filed not later than 15 days after the end of each month.\n**(5) Review**\nAll final determinations of the Commissioner under this subsection shall be reviewable according to the procedures set out in section 205 of the Social Security Act ( 42 U.S.C. 405 ).\n##### (g) Relationship with State law; employer benefits\n**(1) In general**\nThis section does not preempt or supersede any provision of State or local law that authorizes a State or local municipality to provide paid family and medical leave benefits similar to the benefits provided under this section.\n**(2) Greater benefits allowed**\nNothing in this Act shall be construed to diminish the obligation of an employer to comply with any contract, collective bargaining agreement, or any employment benefit program or plan that provides greater paid leave or other leave rights to employees than the rights established under this Act.\n##### (h) Employment and benefits protection and enforcement\n**(1) Employment and benefits protection**\n**(A) In general**\n**(i) Prohibited acts**\nIt shall be unlawful for any person to interfere with, restrain, deny, or retaliate against an individual because of the exercise of, or the attempt to exercise, any right provided under this section, including through\u2014\n**(I)**\ndischarging or in any other manner discriminating against (including retaliating against) an individual because the individual has applied for, indicated an intent to apply for, or received family and medical leave insurance benefits; or\n**(II)**\nusing the application for or the receipt of such benefits as a negative factor in an employment action.\n**(ii) Restoration to position**\nIt shall be interference with the right of an individual for purposes of clause (i) for an employer of the individual to, upon the conclusion of any leave for which the individual received a family and medical leave insurance benefit under this section, fail to\u2014\n**(I)**\nrestore the individual to the position of employment held by the individual when the leave commenced; or\n**(II)**\nrestore the individual to an equivalent position with equivalent employment benefits, pay, and other terms and conditions of employment.\n**(iii) Maintenance of health benefits**\nIt shall be interference with the right of an individual for purposes of clause (i) for an employer of the individual to fail to maintain, for the duration of any leave for which the individual received a family and medical leave insurance benefit under this section, coverage of the individual under any group health plan (as defined in section 5000(b)(1) of the Internal Revenue Code of 1986) at the level and under the conditions coverage would have been provided if the individual had continued in employment continuously for the duration of such leave.\n**(B) Opposing unlawful practices**\nIt shall be unlawful for any employer to discharge or in any other manner discriminate against any individual for opposing any practice made unlawful by this subsection.\n**(C) Interference with proceedings or inquiries**\nIt shall be unlawful for any person to discharge or in any other manner discriminate against any individual because such individual\u2014\n**(i)**\nhas filed any charge, or has instituted or caused to be instituted any proceeding, under or related to this subsection;\n**(ii)**\nhas given, or is about to give, any information in connection with any inquiry or proceeding relating to any right provided under this section; or\n**(iii)**\nhas testified, or is about to testify, in any inquiry or proceeding relating to any right provided under this section.\n**(D) Rebuttable presumption of retaliation**\nAny adverse action (including any action described in subparagraph (C) or (D)) taken against an employee within 12 months of the employee taking any leave for which the individual received a family and medical leave insurance benefit under this section shall establish a rebuttable presumption that the action of the employer is retaliating against such employee in violation of subparagraph (A)(i).\n**(E) Non-application for new hires**\nClauses (ii) and (iii) of subparagraph (A) shall not apply to any individual during the 90-day period beginning with the day the individual begins work for an employer.\n**(2) Civil action by an individual**\n**(A) Liability**\nAny person who violates paragraph (1) shall be liable to any individual employed by such person who is affected by the violation\u2014\n**(i)**\nfor damages equal to the sum of\u2014\n**(I)**\nthe amount of\u2014\n**(aa)**\nany wages, salary, employment benefits, or other compensation denied or lost to such individual by reason of the violation; or\n**(bb)**\nin a case in which wages, salary, employment benefits, or other compensation have not been denied or lost to the individual, any actual monetary losses sustained by the individual as a direct result of the violation, such as the cost of providing care, up to a sum equal to 60 calendar days of wages or salary for the individual;\n**(II)**\nthe interest on the amount described in subclause (I) calculated at the prevailing rate; and\n**(III)**\nan additional amount as liquidated damages equal to the sum of the amount described in subclause (I) and the interest described in subclause (II), except that if a person who has violated paragraph (1) proves to the satisfaction of the court that the act or omission which violated paragraph (1) was in good faith and that the person had reasonable grounds for believing that the act or omission was not a violation of paragraph (1), such court may, in the discretion of the court, reduce the amount of the liability to the amount and interest determined under subclauses (I) and (II), respectively; and\n**(ii)**\nfor such equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n**(B) Right of action**\nAn action to recover the damages or equitable relief prescribed in subparagraph (A) may be maintained against any person in any Federal or State court of competent jurisdiction by any individual for and on behalf of\u2014\n**(i)**\nthe individual; or\n**(ii)**\nthe individual and other individuals similarly situated.\n**(C) Fees and costs**\nThe court in such an action shall, in addition to any judgment awarded to the plaintiff, allow a reasonable attorney's fee, reasonable expert witness fees, and other costs of the action to be paid by the defendant.\n**(D) Limitations**\nThe right provided by subparagraph (B) to bring an action by or on behalf of any individual shall terminate\u2014\n**(i)**\non the filing of a complaint by the Commissioner in an action under paragraph (5) in which restraint is sought of any further delay in the payment of the amount described in subparagraph (A)(I) to such individual by the person responsible under subparagraph (A) for the payment; or\n**(ii)**\non the filing of a complaint by the Commissioner in an action under paragraph (3) in which a recovery is sought of the damages described in subparagraph (A)(I) owing to an individual by a person liable under subparagraph (A),\nunless the action described in clause (i) or (ii) is dismissed without prejudice on motion of the Commissioner.\n**(3) Action by the Commissioner**\n**(A) Civil action**\nThe Commissioner may bring an action in any court of competent jurisdiction to recover the damages described in paragraph (2)(A)(I).\n**(B) Sums recovered**\nAny sums recovered by the Commissioner pursuant to subparagraph (A) shall be held in a special deposit account and shall be paid, on order of the Commissioner, directly to each individual affected. Any such sums not paid to an individual because of inability to do so within a period of 3 years shall be deposited into the Federal Family and Medical Leave Insurance Trust Fund.\n**(4) Limitation**\n**(A) In general**\nAn action may be brought under this subsection not later than 3 years after the date of the last event constituting the alleged violation for which the action is brought.\n**(B) Commencement**\nAn action brought by the Commissioner under this subsection shall be considered to be commenced on the date when the complaint is filed.\n**(5) Action for Injunction by Commissioner**\nThe district courts of the United States shall have jurisdiction, for cause shown, in an action brought by the Commissioner\u2014\n**(A)**\nto restrain violations of paragraph (1), including the restraint of any withholding of payment of wages, salary, employment benefits, or other compensation, plus interest, found by the court to be due to an individual; or\n**(B)**\nto award such other equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n##### (i) Applicability of certain Social Security Act provisions\nThe provisions of sections 204, 205, 206, and 208 of the Social Security Act shall apply to benefit payments authorized by and paid out pursuant to this section in the same way that such provisions apply to benefit payments authorized by and paid out pursuant to title II of such Act.\n##### (j) Effective date for applications\nApplications described in this section may be filed beginning 18 months after the date of enactment of this Act.\n#### 5. Funding for State administration option for legacy States\n##### (a) In general\n**(1) Payments to legacy States**\nIn each calendar year beginning with calendar year 2027, the Commissioner shall make a grant to each State that, for the calendar year preceding such calendar year, was a legacy State and that met the data sharing requirements of subsection (e), in an amount equal to the lesser of\u2014\n**(A)**\nan amount, as estimated by the Commissioner, equal to the total amount of comprehensive paid leave benefits that would have been paid under section 4 (including the costs to the Commissioner to administer such benefits, not to exceed (for purposes of estimating such total amount under this subparagraph) 7 percent of the total amount of such benefits paid) to individuals who received paid family and medical leave benefits under a State law described in paragraph (1) or (3) of subsection (b) during the calendar year preceding such calendar year if the State had not been a legacy State for such preceding calendar year; or\n**(B)**\nan amount equal to the total cost of paid family and medical leave benefits under a State law described in paragraph (1) or (3) of subsection (b) for the calendar year preceding such calendar year, including\u2014\n**(i)**\nany paid family and medical leave benefits provided by an employer (whether directly, under a contract with an insurer, or provided through a multiemployer plan) as described in subsection (d); and\n**(ii)**\nthe full cost to the State of administering such law (except that such cost may not exceed 7 percent of the total amount of paid family and medical leave benefits paid under such State law).\n**(2) Estimated payments**\nIn any case in which, during any calendar year, the Commissioner has reason to believe that a State will be a legacy State and meet the data sharing requirements of subsection (e) for such calendar year, the Commissioner may make estimated payments during such calendar year of the grant which would be paid to such State in the succeeding calendar year, to be adjusted as appropriate in the succeeding calendar year.\n##### (b) Legacy State\nFor purposes of this section, the term legacy State for a calendar year means a State with respect to which the Commissioner determines that\u2014\n**(1)**\nthe State has enacted, not later than the date of enactment of this Act, a State law that provides paid family and medical leave benefits;\n**(2)**\nfor any calendar year that begins before the date that is 3 years after the date of enactment of this Act, the State certifies to the Commissioner that the State intends to remain a legacy State and meet the data sharing requirements of subsection (e) at least through the first calendar year that begins on or after such date; and\n**(3)**\nfor any calendar year that begins on or after such date, a State law of the State provides for a State program to remain in effect throughout such calendar year that provides comprehensive paid family and medical leave benefits (which may be paid directly by the State or, if permitted under such State law, by an employer pursuant to such State law)\u2014\n**(A)**\nfor at least 12 full workweeks of leave during each 12-month period to at least all of those individuals in the State who would be eligible for comprehensive paid leave benefits under section 4 (without regard to section 2(5)(C)), except that the State shall provide such benefits for leave from employment by the State or any political subdivision thereof, and may elect to provide such benefits for leave from any other governmental employment; and\n**(B)**\nat a wage replacement rate that is at least equivalent to the wage replacement rate under the comprehensive paid leave benefit program under section 4 (without regard to section 2(5)(C)).\n##### (c) Covered employment under the law of a legacy State\nFor purposes of this Act, the term covered employment under the law of a legacy State means employment (or self-employment) with respect to which an individual would be eligible to receive paid family and medical benefits under the State law of a State, as described in paragraph (1) or (3) of subsection (b), during any period during which such State is a legacy State.\n##### (d) Employer-Provided benefits in a legacy State\n**(1) Treatment for purposes of this title**\nIn the case of a State that permits paid family and medical leave benefits to be provided by an employer (whether directly, under a contract with an insurer, or provided through a multiemployer plan) pursuant to a State law described in paragraph (1) or (3) of subsection (b)\u2014\n**(A)**\nsuch benefits shall be considered, for all purposes under this Act, paid family and medical leave benefits under the law of a legacy State; and\n**(B)**\nleave for which such benefits are paid shall be considered, for all such purposes, leave from covered employment under the law of a legacy State.\n**(2) Distribution of grant funds**\nIn any case in which paid family and medical leave benefits are provided by 1 or more employers (whether directly, under a contract with an insurer, or provided through a multiemployer plan) in a legacy State pursuant to a State law described in paragraph (1) or (3) of subsection (b), the State, upon the receipt of any grant amount under subsection (a), may distribute an appropriate share of such grant to each such employer.\n##### (e) Data sharing\nAs a condition of receiving a grant under subsection (a) in a calendar year, a State shall enter into an agreement with the Commissioner under which the State shall provide the Commissioner\u2014\n**(1)**\nwith information, to be provided periodically as determined by the Commissioner, concerning individuals who received a paid leave benefit under a State law described in paragraph (1) or (3) of subsection (b), including\u2014\n**(A)**\neach individual\u2019s name;\n**(B)**\ninformation to establish the individual\u2019s identity;\n**(C)**\ndates for which such paid leave benefits were paid;\n**(D)**\nthe amount of such paid leave benefit; and\n**(E)**\nto the extent available, such other information concerning such individuals as necessary for the purpose of carrying out this section and section 2(5)(C);\n**(2)**\nnot later than July 1 of such calendar year, the amount needed to adjust payments as described in subsection (a)(2) for the calendar year preceding such calendar year; and\n**(3)**\nsuch other information as needed to determine compliance with grant requirements.\n#### 6. Regulations\nThe Commissioner, in consultation with the Secretary of Labor, shall prescribe regulations necessary to carry out this Act. In developing such regulations, the Commissioner shall consider the input from a volunteer advisory body comprised of not more than 15 individuals, including experts in the relevant subject matter and officials charged with implementing State paid family and medical leave insurance programs. The Commissioner shall take such programs into account when proposing regulations. Such individuals shall be appointed as follows:\n**(1)**\nFive individuals to be appointed by the President.\n**(2)**\nThree individuals to be appointed by the majority leader of the Senate.\n**(3)**\nTwo individuals to be appointed by the minority leader of the Senate.\n**(4)**\nThree individuals to be appointed by the Speaker of the House of Representatives.\n**(5)**\nTwo individuals to be appointed by the minority leader of the House of Representatives.\n#### 7. GAO Study\n##### (a) Study\nAs soon as practicable after calendar year 2026, and every 5 years thereafter, the Comptroller General shall submit to Congress a report on family and medical leave insurance benefits paid under section 4 for any month during the covered period. The report shall include the following:\n**(1)**\nAn identification of the total number of applications for such benefits filed for any month during the covered period, and the average number of days occurring in the period beginning on the date on which such an application is received and ending on the date on which the initial determination of eligibility with respect to the application is made.\n**(2)**\nAn identification of the total number of requests for review of an initial adverse determination of eligibility for such benefits made during the covered period, and the average number of days occurring in the period beginning on the date on which such review is requested and ending on the date on which the final determination of eligibility with respect to such review is made.\n**(3)**\nAn identification of the total number of monthly benefit claim reports for such benefits filed during the covered period, and the average number of days occurring in the period beginning on the date on which such a claim report is received and ending on the date on which the initial determination of eligibility with respect to the claim report is made.\n**(4)**\nAn identification of the total number of requests for review of an initial adverse determination relating to a monthly benefit claim report for such benefits made during the covered period, and the average number of days occurring in the period beginning on the date on which such review is requested and ending on the date on which the final determination of eligibility with respect to such review is made.\n**(5)**\nAn identification of any excessive delay in any of the periods described in paragraphs (1) through (4), including\u2014\n**(A)**\na description of the causes for such delay; or\n**(B)**\ninformation any correlation in such delay to claimant demographics, industry sector, or qualifying reason.\n**(6)**\nAn identification of any additional data that needs to be collected as part of the application process for benefits to produce the report required under this section.\n##### (b) Covered period\nIn this section, the term covered period means\u2014\n**(1)**\nwith respect to the report due as soon as practicable after calendar year 2026, such calendar year; and\n**(2)**\nwith respect to the report due every 5 years thereafter, the 5-calendar year period ending on December 31 of the year prior to the year in which such report is due.",
      "versionDate": "2025-09-16",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-09-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2823",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FAMILY Act",
      "type": "S"
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-25T14:34:37Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5390ih.xml"
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
      "title": "FAMILY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAMILY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Family and Medical Insurance Leave Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide paid family and medical leave benefits to certain individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T09:18:31Z"
    }
  ]
}
```
