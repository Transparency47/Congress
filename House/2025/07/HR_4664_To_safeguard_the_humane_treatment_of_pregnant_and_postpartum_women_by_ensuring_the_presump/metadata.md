# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4664?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4664
- Title: Stop Shackling and Detaining Pregnant Women Act
- Congress: 119
- Bill type: HR
- Bill number: 4664
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-14T08:08:07Z
- Update date including text: 2026-05-14T08:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4664",
    "number": "4664",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000587",
        "district": "29",
        "firstName": "Sylvia",
        "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
        "lastName": "Garcia",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Stop Shackling and Detaining Pregnant Women Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:07Z",
    "updateDateIncludingText": "2026-05-14T08:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:13:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MS"
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
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NM"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
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
      "sponsorshipDate": "2025-07-23",
      "state": "DC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NJ"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CO"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "AL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IN"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "LA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MO"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
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
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "AL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NM"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "HI"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "AZ"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NJ"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NY"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
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
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4664ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4664\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Garcia of Texas (for herself, Mr. Thompson of Mississippi , Ms. Vel\u00e1zquez , Mr. Takano , Ms. Waters , Mr. Espaillat , Ms. Clarke of New York , Ms. Leger Fernandez , Mr. Castro of Texas , Mrs. Ramirez , Mr. Johnson of Georgia , Ms. Norton , Mr. Evans of Pennsylvania , Mrs. Watson Coleman , Ms. DeGette , Mr. Davis of Illinois , Ms. Sewell , Ms. Simon , Ms. Tlaib , Mr. Carson , Mr. Krishnamoorthi , Mr. Correa , Ms. Ross , Mr. Vargas , Ms. Williams of Georgia , Mr. Fields , Ms. Crockett , Ms. Wilson of Florida , Mr. Bell , Ms. Schakowsky , Mr. Green of Texas , Ms. Kelly of Illinois , Ms. Omar , Mr. Thanedar , Mr. Goldman of New York , Mr. Jackson of Illinois , Ms. Barrag\u00e1n , Ms. McCollum , Mr. Khanna , Mr. Soto , Mr. Figures , Ms. Lee of Pennsylvania , Ms. Brownley , Mr. Garc\u00eda of Illinois , and Ms. Ocasio-Cortez ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo safeguard the humane treatment of pregnant and postpartum women by ensuring the presumption of release and prohibiting shackling, restraining, and other inhumane treatment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Shackling and Detaining Pregnant Women Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Appropriations of the Senate ;\n**(D)**\nthe Committee on Homeland Security of the House of Representatives ;\n**(E)**\nthe Committee on the Judiciary of the House of Representatives ; and\n**(F)**\nthe Committee on Appropriations of the House of Representatives .\n**(2) Commissioner**\nThe term Commissioner means the Commissioner for U.S. Customs and Border Protection.\n**(3) Detained noncitizen**\nThe term detained noncitizen includes any adult or juvenile individual detained by any Federal, State, or local law enforcement agency (including under contract or agreement with such agency) under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(4) Detention officer**\nThe term detention officer means an individual who\u2014\n**(A)**\nworks at a facility, including an individual who works at a facility pursuant to a contract or subcontract; and\n**(B)**\nperforms duties relating to the security, custody, or transport of individuals in custody.\n**(5) Director**\nThe term Director means the Director for U.S. Immigration and Customs Enforcement.\n**(6) Facility**\nThe term facility means a Federal, State, or local government facility, or a privately owned and operated facility, that is used, in whole or in part, to hold individuals under the authority of the Secretary of Homeland Security, including a facility that\u2014\n**(A)**\nholds such individuals under a contract or agreement with the Director or the Commissioner; or\n**(B)**\nis used, in whole or in part, to hold individuals pursuant to an immigration detainer or similar request.\n**(7) Facility administrator**\nThe term facility administrator means the official responsible for oversight of a facility, or the designee of such official.\n**(8) Postpartum**\nThe term postpartum means during the 1-year period, or longer, as determined by the licensed health care provider of the individual concerned, following delivery, including the entire period during which the individual is in a medical facility, birthing center, or infirmary after birth.\n**(9) Restraint**\nThe term restraint \u2014\n**(A)**\nmeans any physical restraint or mechanical device used to control the movement of the body or limbs of a detained noncitizen\u2019s body for custody purposes, including\u2014\n**(i)**\nflex cuffs;\n**(ii)**\nsoft restraints;\n**(iii)**\nhard metal handcuffs;\n**(iv)**\na black box;\n**(v)**\nChubb cuffs;\n**(vi)**\nleg irons;\n**(vii)**\nbelly chains;\n**(viii)**\na security (tether) chain;\n**(ix)**\na convex shield; and\n**(x)**\nany other type of shackles; and\n**(B)**\ndoes not include medical restraints.\n**(10) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 3. Limitation on detention of pregnant women and mothers of newborns\n##### (a) Access to pregnancy testing\nThe Secretary shall provide every individual being processed into custody access to pregnancy testing during the initial medical screening.\n##### (b) Presumption of release\n**(1) In general**\nExcept as provided in paragraph (2), the Secretary\u2014\n**(A)**\nmay not detain, arrest, or take into custody an individual under any provision of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) who is known to be pregnant, lactating, or postpartum, pending a decision with respect to whether the noncitizen is to be removed from the United States; and\n**(B)**\nshall immediately release any detained noncitizen found to be pregnant.\n**(2) Exceptions**\nThe Secretary, pursuant to chapter 4 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1221 et seq. ), may detain an individual who is known to be pregnant, lactating, or postpartum\u2014\n**(A)**\nunder extraordinary circumstances in which the Secretary makes an individualized determination that credible, reasonable grounds exist to believe that\u2014\n**(i)**\nsuch individual poses an immediate and serious risk of physical harm to others; and\n**(ii)**\nenrollment in an alternative to detention program cannot mitigate public safety threats associated with such individual; and\n**(B)**\nif such detention is the only means available to mitigate such threats.\n**(3) Removal**\nIf detention is the only means of effectuating the removal from the United States of a pregnant individual subject to a final order of deportation or removal, the Secretary, solely for the purpose of such deportation or removal, may detain the pregnant individual in temporary housing in accordance with applicable temporary housing standards for a period equal to the shorter of\u2014\n**(A)**\nthe shortest possible period immediately preceding the deportation or removal of the individual from the United States; and\n**(B)**\n5 days.\n##### (c) Weekly review\n**(1) In general**\nThe Secretary shall conduct an individualized review of each noncitizen detained pursuant to subsection (b)(2) not less frequently than weekly to determine whether such noncitizen continues to be subject to detention under such subsection. Each such review shall be completed within 72 hours after being initiated.\n**(2) Release**\nNot later than 24 hours after the Secretary determines pursuant to paragraph (1) that a pregnant noncitizen is no longer subject to detention under subsection (b)(2), the noncitizen shall be released from the facility in which the noncitizen had been detained in accordance with safe release standards. In carrying out such release, an officer at such facility shall\u2014\n**(A)**\nprepare the noncitizen\u2019s complete medical records, medications, and any supplies required to maintain the noncitizen's state of health until the noncitizen can be seen by a community health professional; and\n**(B)**\ncommunicate with the noncitizen's attorney of record, sponsor, or any post-release service provider as soon as details of the noncitizen's planned release are available.\n#### 4. Humane treatment of pregnant detained noncitizens while in detention and custody\n##### (a) Prohibition on restraint of pregnant detained noncitizens\n**(1) Prohibition**\nExcept as provided in paragraph (2), restraints may not be used on a noncitizen who is in the physical custody of the Department of Homeland Security, including during transport, if the noncitizen is known to be\u2014\n**(A)**\npregnant, including during labor and delivery;\n**(B)**\nlactating; or\n**(C)**\npostpartum.\n**(2) Exceptions**\n**(A) In general**\nNotwithstanding paragraph (1), and subject to subparagraph (B), use of a restraint on a detained noncitizen described in paragraph (1) may be permitted only in an extraordinary circumstance, except in the case of a medical contraindication, in which the facility administrator has ordered the use of the restraint after making an individualized determination that\u2014\n**(i)**\ncredible, reasonable grounds exist to believe the detained noncitizen poses an immediate and serious risk of physical harm to others; or\n**(ii)**\nreasonable grounds exist to believe the detained noncitizen presents an immediate and credible risk of escape that cannot be reasonably minimized through any other method.\n**(B) Requirement for least restrictive restraints**\nIn the rare event of an extraordinary circumstance described in subparagraph (A), only the least restrictive restraint necessary shall be used, except that\u2014\n**(i)**\nif a doctor, nurse, or other health professional treating a detained noncitizen requests that a restraint not be used, the detention officer accompanying the detained noncitizen shall immediately remove any restraint; and\n**(ii)**\nunder no circumstance shall\u2014\n**(I)**\na leg, waist, or 4-point restraint be used;\n**(II)**\na wrist restraint be used to bind the hands of such a detained noncitizen behind the back of the detained noncitizen or to another individual;\n**(III)**\na detained noncitizen be restrained in a face-down position or on their back; or\n**(IV)**\nany restraint be used on any detained noncitizen who is in labor or delivering.\n**(3) Record of extraordinary circumstances**\n**(A) Requirements**\nIf a restraint is used on a detained noncitizen pursuant to paragraph (2)(A), not later than 5 days after the date on which the restraint was used, the facility administrator shall\u2014\n**(i)**\nrecord in writing the finding that describes the medical purpose or extraordinary circumstance that dictated the use of the restraint; and\n**(ii)**\nsubmit the finding to the Director.\n**(B) Retention**\n**(i) Facility**\nWith respect to a written finding under subparagraph (A)(i), the facility administrator shall\u2014\n**(I)**\nkeep the finding on file at the applicable facility for not less than 5 years after the date on which the restraint was used; and\n**(II)**\nmake a copy of the finding available for public inspection on request, only after making appropriate redactions so as to protect personally identifiable information.\n**(ii) U.S. immigration and customs enforcement**\nThe Director shall maintain a written finding submitted to the Director pursuant to subparagraph (A)(ii) and make such finding available for public inspection only after making appropriate redactions to protect personally identifiable information.\n##### (b) Prohibition on presence of nonmedical staff\n**(1) In general**\nExcept as provided in paragraph (2), nonmedical staff may not be present in a room in which a pelvic or breast exam, labor, delivery (whether vaginal or by cesarean delivery), or treatment of any other symptom relating to a pregnancy of a detained noncitizen is occurring unless their presence is specifically requested by medical personnel and only for a duration that is actually required to fulfill such request.\n**(2) Exception**\nIf the presence of nonmedical staff is requested by medical personnel, the nonmedical staff shall\u2014\n**(A)**\nbe of the detained noncitizen\u2019s gender of choice, if practicable; and\n**(B)**\nremain at a reasonable distance from the detained noncitizen and face toward the detained noncitizen\u2019s head to protect the privacy of the detained noncitizen.\n**(3) Use of restraints**\nIf a restraint is used on a detained noncitizen pursuant to subsection (a)(2)(A), an employee of the Department of Homeland Security shall remain immediately outside the room at all times so that the employee may promptly remove the restraint if requested by medical personnel pursuant to subsection (a)(2)(B)(i).\n##### (c) Access to services\n**(1) U.S. immigration and customs enforcement custody**\nA detained noncitizen in the custody of U.S. Immigration and Customs Enforcement shall have access to health care services, including comprehensive counseling and services relating to reproductive health care and pregnancy, including\u2014\n**(A)**\nroutine and specialized prenatal care, including adequate nutrition and exercise, HIV testing and treatment, and prenatal vitamins and vaccines;\n**(B)**\nlabor and delivery;\n**(C)**\ntreatment for complications from pregnancy;\n**(D)**\nsubstance use disorder treatment;\n**(E)**\npostpartum physical and mental health care, including postpartum reversible contraceptive methods;\n**(F)**\nno-cost supply of menstrual hygiene products;\n**(G)**\nlactation services; and\n**(H)**\nfamily planning, continuation of pre-detention contraceptive methods, and abortion services.\n**(2) U.S. customs and border protection custody**\nThe Commissioner shall ensure that minimum standards of care are met for pregnant detained noncitizens who are in the custody of U.S. Customs and Border Protection.\n##### (d) Requirement for informed medical consent\nServices described in subsection (c)(1) may not be performed on a detained noncitizen until the provider of such services obtains informed consent from the noncitizen. Medical treatment may not be administered to a detained noncitizen against such noncitizen\u2019s will.\n##### (e) Medical center arrangements\nEach facility administrator shall maintain\u2014\n**(1)**\nan arrangement with the nearest maternity hospital and ensure facility staff know where to take pregnant detained noncitizens in case of emergency; and\n**(2)**\na policy to ensure the provision of proper care if a detained noncitizen cannot be moved with immediacy to a medical center.\n#### 5. Notice of rights and training\n##### (a) Notice of detained noncitizen rights\nThe Secretary shall provide to each detained noncitizen, in a language or manner that such noncitizen can understand, notice of the detained noncitizen\u2019s rights under this Act.\n##### (b) Training for Department of Homeland Security employees\nAt the time of hiring, and annually thereafter, the Secretary shall provide training regarding the requirements under this Act to each employee of the Department of Homeland Security who is involved in the detention or care of a pregnant detained noncitizen or a postpartum parent of a newborn who is being detained pursuant to chapter 4 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1221 et seq. ).\n#### 6. Reports; rulemaking\n##### (a) Reports\n**(1) Reports by facility administrators**\nNot later than 30 days after the end of each calendar quarter, the facility administrator of each detention facility in which 1 or more pregnant noncitizens were detained during such quarter shall submit a written report to the Secretary that includes, with respect to the facility during such quarter\u2014\n**(A)**\nan account of every instance of the use of a restraint on a pregnant detained noncitizen during pregnancy, labor, or postpartum recovery, including\u2014\n**(i)**\nthe type of restraint;\n**(ii)**\nthe justification for the use of such restraint; and\n**(iii)**\nthe name of the facility administrator who made the individualized determination pursuant to section 4(a)(2)(A);\n**(B)**\nthe number of pregnant noncitizens held at such facility;\n**(C)**\nthe number of released pregnant noncitizens who were held at such facility;\n**(D)**\nthe average length of detention of pregnant noncitizens;\n**(E)**\nthe number of pregnant noncitizens who were detained for between 15 and 30 days;\n**(F)**\nthe number of pregnant noncitizens who were detained longer than 30 days; and\n**(G)**\nthe number of pregnant noncitizens who gave birth while detained and a description of the outcomes of any pregnancies that ended in custody, including any pregnancy that resulted in a live birth, a stillbirth, a miscarriage, an abortion, an ectopic pregnancy, maternal morbidity, maternal death, neonatal death, or preterm birth.\n**(2) Audit and reports by Secretary**\nNot later than 90 days after the last day of each fiscal year, the Secretary shall\u2014\n**(A)**\ncomplete an audit of the information described in subparagraphs (B) through (E) of paragraph (1) contained in reports covering such fiscal year;\n**(B)**\nsubmit a report to the appropriate committees of Congress that includes a summary of the information submitted pursuant to paragraph (1), disaggregated by facility; and\n**(C)**\nissue regulations in accordance with relevant national standards that set minimum standards for facilities providing medical care to pregnant noncitizens.\n**(3) Privacy**\nNone of the reports submitted pursuant to paragraph (1) or (2) may contain the individually identifying information of any detained noncitizen or the noncitizen's health care provider.\n**(4) Public inspection**\n**(A) In general**\nExcept as provided in subparagraph (B), each report submitted under this subsection shall be made available on a publicly accessible website of the relevant agency.\n**(B) Facility administrator**\nNone of the reports submitted under paragraph (1) or (2) that is posted on a publicly accessible website may contain the name of the facility administrator referred to in paragraph (1)(A)(iii).\n##### (b) Rulemaking\nThe Secretary shall adopt regulations or policies to implement the requirements under this Act at each detention facility managed or overseen by the Department of Homeland Security.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-03-10",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "916",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Shackling and Detaining Pregnant Women Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-17T17:13:56Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4664ih.xml"
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
      "title": "Stop Shackling and Detaining Pregnant Women Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Shackling and Detaining Pregnant Women Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To safeguard the humane treatment of pregnant and postpartum women by ensuring the presumption of release and prohibiting shackling, restraining, and other inhumane treatment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:31Z"
    }
  ]
}
```
